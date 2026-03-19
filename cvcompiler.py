import jinja2
from enum import Enum
from dataclasses import dataclass, field
from typing import List, Union, Optional
import re
import pandoc
from collections.abc import Iterable
# Hi
# Here I am playing A LOT with the __str__ thing


# some utilities

cplusplus = re.compile(r"\bC\+\+", re.IGNORECASE)
bhplusplus = re.compile(r"\bBH\+\+", re.IGNORECASE)
ampersand = re.compile(r"[^\\]&")


def iterate(x):
    if isinstance(x, Iterable) and not isinstance(x, str):
        return x
    return [x]


LANGUAGE = "ita"


def set_language(language: str):
    global LANGUAGE
    match language.lower():
        case "ita":
            LANGUAGE = "ita"
        case "eng":
            LANGUAGE = "eng"
        case _:
            raise ValueError(f"language {language} is not supported")


SLIM_EDUCATION: bool = False


def set_slim_education(toggle: bool):
    global SLIM_EDUCATION
    # wy not SLIM_EDUCATION=toggle? -> I want to be sure that SLIM_EDUCATION is boolean in this funny word of duck typing
    if toggle:
        SLIM_EDUCATION = True
    else:
        SLIM_EDUCATION = False


class CVType(Enum):
    MODERN = 0
    ALTA = 1


CVTYPE = CVType.MODERN


def set_template_type(templatename: str):
    global CVTYPE

    match templatename.lower():
        case "modern":
            CVTYPE = CVType.MODERN
        case "alta":
            CVTYPE = CVType.ALTA
        case _:
            raise ValueError(f"Unknown document type: {templatename}")


# to future me: frozen=True make this hashable
@dataclass(frozen=True)
class Translate:
    ita: str
    eng: str

    def __str__(self) -> str:
        match LANGUAGE:
            case "ita":
                return self.ita
            case "eng":
                return self.eng
            case _:
                raise ValueError(f"language {LANGUAGE} is not supported")


def cleanAmpersand(text: str):
    return ampersand.sub(r"\\&{}", str(text))


def beautifyCpp(text: str):
    return cplusplus.sub(r"\\CC{}", bhplusplus.sub(r"\\BHpp{}", text))


def latexify(markdown: str):
    doc = pandoc.read(str(markdown))
    latex = pandoc.write(doc, format="latex")
    # smoothing some command that are not defined in moderncv:
    return latex.replace(r"\item" "\n", r"\item ").replace(
        r"\begin{itemize}" "\n" r"\tightlist", r"\begin{itemize}"
    )


# Work and education
@dataclass
class CVEntry:
    date_start: str
    date_end: str
    job_title: str
    employer: str
    city: str = field(default_factory=str)
    grade: str = field(default_factory=str)
    description: str = field(default_factory=str)

    def __post_init__(self):
        self.city = self.city or ""
        self.grade = self.grade or ""

        for name, value in [
            ("date_start", self.date_start),
            ("date_end", self.date_end),
            ("job_title", self.job_title),
            ("employer", self.employer),
        ]:
            if value is None:
                raise ValueError(f"'{name}' can't be None.")
            if (
                name in {"date_start", "job_title", "employer"}
                and str(value).strip() == ""
            ):
                raise ValueError(f"'{name}' can't be empty.")

    def __str__(self) -> str:
        # Costruisce la stringa LaTeX con escape dei caratteri speciali
        date_range = f"{self.date_start} - {self.date_end}"

        desc = (
            beautifyCpp(latexify(self.description))
            .replace("\n\n", r"\newline{}")
            # this avoids error with a newline after the end of the itemize
            .replace(r"\end{itemize}\newline{}", r"\end{itemize}")
        )
        return (
            rf"\cventry{{{date_range}}}"
            f"{{{self.job_title}}}"
            f"{{{self.employer}}}"
            f"{{{self.city}}}"
            f"{{{self.grade}}}"
            f"{{{desc}}}"
        )


@dataclass
class CVEvent:
    date_start: str
    date_end: str
    job_title: str
    employer: str
    city: str = field(default_factory=str)
    description: str = field(default_factory=str)

    def __post_init__(self):
        self.city = self.city or ""

        for name, value in [
            ("date_start", self.date_start),
            ("date_end", self.date_end),
            ("job_title", self.job_title),
            ("employer", self.employer),
        ]:
            if value is None:
                raise ValueError(f"'{name}' can't be None.")
            if (
                name in {"date_start", "job_title", "employer"}
                and str(value).strip() == ""
            ):
                raise ValueError(f"'{name}' can't be empty.")

    def __str__(self) -> str:
        # Costruisce la stringa LaTeX con escape dei caratteri speciali
        date_range = f"{self.date_start} - {self.date_end}"

        desc = (
            beautifyCpp(latexify(self.description))
            .replace("\n\n", r"\newline{}")
            # this avoids error with a newline after the end of the itemize
            .replace(r"\end{itemize}\newline{}", r"\end{itemize}")
        )
        # Hipster:
        return (
            rf"\cvevent{{{self.job_title}}}"
            f"{{{self.employer}}}"
            f"{{{date_range}}}"
            f"{{{self.city}}}"
            f"\n{desc}"
        )


@dataclass
class Education:
    degree: str
    date_start: str
    date_end: str
    institution: str
    city: str
    grade: str
    title: str
    eqf: int
    field: str
    description: Optional[str | Translate] = None

    def __str__(self):
        match CVTYPE:
            case CVType.MODERN:
                # made this a function to ensure that the str method is postponed
                # at the time of running the jinja template
                desc = f"**EQF**: {self.eqf} **{Translate(ita='Campo', eng='Field')}**: _{self.field}_ \n\n"
                desc += (
                    rf"**{Translate(ita='Titolo', eng='Title')}**: _{self.title}_" "\n"
                )
                if self.description and not SLIM_EDUCATION:
                    desc += "\n" + str(self.description)

                return str(
                    CVEntry(
                        self.date_start,
                        self.date_end,
                        self.degree,
                        self.institution,
                        self.city,
                        self.grade,
                        desc,
                    )
                )
            case CVType.ALTA:
                return str(
                    CVEvent(
                        self.date_start,
                        self.date_end,
                        self.degree,
                        self.institution,
                        self.city,
                        self.title,
                    )
                )


@dataclass()
class WorkExperience:
    title: str
    date_start: str
    date_end: str
    employer: str
    city: str = None
    description: str | Translate = None

    def __str__(self):
        match CVTYPE:
            case CVType.MODERN:
                return str(
                    CVEntry(
                        self.date_start,
                        self.date_end,
                        self.title,
                        self.employer,
                        self.city,
                        None,
                        self.description,
                    )
                )
            case CVType.ALTA:
                return str(
                    CVEvent(
                        self.date_start,
                        self.date_end,
                        self.title,
                        self.employer,
                        self.city,
                        self.description,
                    )
                )


# Skills

# Usage: export a list of skills in the jinja template to create a skill table
# or export a list of skillsets to have a less detailed, but more compact list of skills


@dataclass
class Skill:
    skill: str
    level: str = ""
    description: str = ""
    emph: bool = False
    startCategory: bool = False  #: this is to be used in a skill matrix

    def __post_init__(self):
        match self.skill.lower():
            case "c++":
                # https://isocpp.org/wiki/faq/misc-environmental-issues#latex-macros
                self.skill = r"\CC"
            case "latex":
                self.skill = r"\LaTeX{}"

    def __str__(self) -> str:
        if self.startCategory:
            return (
                rf"\cvskillentry*{{{self.skill}}}{{{self.level}}}{{{self.description}}}"
            )
        else:
            return (
                rf"\cvskillentry{{{self.skill}}}{{{self.level}}}{{{self.description}}}"
            )


class SkillSet:
    title: str
    _skills: list[Skill]

    def __init__(self, title, *args):
        self.title = title
        self._skills = []
        for s in args:
            assert type(s) is Skill
            self._skills.append(s)

    def toList(self):
        toret = []
        for s in self._skills:
            if s.emph:
                toret.append(rf"\textbf{{{s.skill}}}")
            else:
                toret.append(s.skill)
        return toret


def skillDict(*sks: list[SkillSet]) -> dict:
    toret = {}
    for sk in sks:
        assert type(sk) is SkillSet
        toret[sk.title] = r" \textbullet{} ".join(sk.toList())
    return toret


# Conferences
@dataclass
class Talk:
    title: str
    invited: bool = False

    def __str__(self):
        return rf"\cvitem{{Talk{' (invited)' if self.invited else ''}}}{{{cleanAmpersand(self.title)}}}"


@dataclass
class Poster:
    title: str
    invited: bool = False

    def __str__(self):
        return rf"\cvitem{{Poster{' (invited)' if self.invited else ''}}}{{{cleanAmpersand(self.title)}}}"


ContributionType = Union[Talk, Poster, List[Union[Talk, Poster]]]


@dataclass
class Conference:
    date: str
    place: str
    title: str
    contribution: ContributionType
    note: str = ""

    def getContributions(self):
        if type(self.contribution) is list:
            return self.contribution
        return [self.contribution]

    def __str__(self):
        data = rf"\subsection{{{cleanAmpersand(self.title)}}}" + "\n\n"
        data += (
            rf"\cvdoubleitem{{}}{{\textit{{[{self.date}]}}}}{{}}{{\textit{{{self.place}}}}}"
            + "\n"
        )
        for cntr in self.getContributions():
            data += str(cntr) + "\n"

        return data


# Languages


@dataclass
class Language:
    language: str
    listening: str
    reading: str
    writing: str
    spoken_production: str
    spoken_interaction: str
    overall_of_five: float


@dataclass
class Languages:
    mother_tongues: str | list[str]
    other_languages: str | list[str]
    showLegend: bool = True

    def __str__(self):
        toret = ""
        match CVTYPE:
            case CVType.MODERN:
                title = Translate(ita="Lingua madre:", eng="Mother tongue:")
                for mt in iterate(self.mother_tongues):
                    toret += rf"\cvitemwithcomment{{{title}:}}{{{mt}}}{{}}"
                    toret += "\n"
                    title = ""
                title = Translate(ita="Altri linguaggi:", eng="Other languages:")

                listening = Translate("Ascolto", "Listening")
                reading = Translate("Lettura", "Reading")
                writing = Translate("Scrittura", "Writing")
                spoken_production = Translate("Produzione orale", "Spoken production")
                spoken_interaction = Translate(
                    "Interazione orale", "Spoken interaction"
                )
                for ot in iterate(self.other_languages):
                    if type(ot) is Language:
                        toret += rf"\cvitemwithcomment{{{title}}}{{{ot.language}}}"
                        toret += (
                            "{"
                            + rf"{listening}~\textbf{{{ot.listening}}}~"
                            + rf"{reading}~\textbf{{{ot.reading}}}~"
                            + rf"{writing}~\textbf{{{ot.writing}}} "
                            + rf"{spoken_production}~\textbf{{{ot.spoken_production}}}~"
                            + rf"{spoken_interaction}~\textbf{{{ot.spoken_interaction}}}"
                            + "}"
                        )

                    else:
                        toret += rf"\cvitemwithcomment{{{title}}}{{{ot}}}{{}}"
                    toret += "\n"
                    title = ""
                if self.showLegend:
                    toret += "\cvitemwithcomment{}{}{" + str(
                        Translate(
                            ita="Livelli: A1 e A2: Livello elementare - B1 e B2: Livello intermedio - C1 e C2: Livello avanzato",
                            eng="Levels: A1 and A2: Basic user - B1 and B2: Independent user - C1 and C2: Proficient user",
                        )
                    )
                    toret += "}"
            case CVType.ALTA:
                for mt in iterate(self.mother_tongues):
                    toret += rf"\cvskill{{{mt}}}{{5}}"
                    toret += "\n"

                for ot in iterate(self.other_languages):
                    if type(ot) is Language:
                        toret += rf"\cvskill{{{ot.language}}}{{{ot.overall_of_five}}}"
                    else:
                        toret += rf"\cvskill{{{ot}}}{{}}"
                    toret += "\n"
        # \divider
        # \cvskill{German}{3.5} %% Supports X.5 values.
        return toret


# the presentation
@dataclass
class Presentation:
    presentation: str

    def __str__(self):
        return beautifyCpp(latexify(self.presentation))


def make_cover_letter(settings: dict):
    # letter setup
    for required in ["recipient", "recipient_address", "subject"]:
        assert required in settings, (
            f'a field callen "{required}" is required for the cover letter'
        )
    letter = (
        rf"\recipient{{{settings['recipient']}}}{{{settings['recipient_address']}}}"
        + "\n"
    )
    date = ""
    if "date" in settings:
        date = settings["date"]
    else:
        from datetime import datetime

        d = datetime.now()
        date = d.strftime("%d %B %Y")

    letter += rf"\date{{{date}}}" + "\n"
    letter += rf"\subject{{{settings['subject']}}}" + "\n"
    opening = (
        settings["opening"]
        if "opening" in settings
        else Translate(
            ita="",
            eng="Dear Sir or Madam",
            # eng="To whom it may concern,"
        )
    )
    letter += rf"\opening{{{opening}}}" + "\n"
    closing = (
        settings["closing"]
        if "closing" in settings
        else Translate(ita="Saluti,", eng="Yours faithfully,")
    )
    letter += rf"\closing{{{closing}}}" + "\n"
    if "signature" in settings:
        # optional, remove / comment the line if not wanted: first argument goes to \includegraphics > scale"
        letter += rf"\signature{{0.9}}{{{settings['signature']}}}"
    # % use an optional argument to use a string other than "Enclosure", or redefine \enclname"
    # letter+=rf"%\enclosure[Attached]{{curriculum vit\ae{}}}
    body = beautifyCpp(latexify(settings["body"]))
    letter += rf"""
\makelettertitle

{body}

\makeletterclosing
"""
    return letter


def create_cv(datain, template="cvtemplate.tex", output="cv.tex"):
    """
    Generate a LaTeX CV by rendering a Jinja2-powered template with structured data.

    This function loads a LaTeX template, prepares a rendering environment with
    custom delimiters, enriches the provided data with multilingual section headers
    using the `Translate` class, renders the document through Jinja2, and finally
    writes the resulting LaTeX code to an output file.

    Parameters
    ----------
    datain : dict
        A dictionary containing all the dynamic data used to fill the CV template.
        Each key should match a variable referenced inside the Jinja2/LaTeX template.
        The value will be converted to string by Jinja

    template_path : str, optional
        Path to the LaTeX `.tex` template file written using custom Jinja2
        delimiters (`<% %>`, `<< >>`, `<# #>`). The file is read as UTF‑8.
        Default is `"cvtemplate.tex"`.

    output_path : str, optional
        Path where the rendered LaTeX document will be saved. The file is written
        as UTF‑8. Default is `"cv.tex"`.


    Section labels are translated
    -----------------------------
    The function inserts the following keys into the data dictionary:

    - `presentationSection` → "Presentazione" / "About me"
    - `educationSection` → "Educazione" / "Education"
    - `digitalSkillsSection` → "Competenze digitali" / "Digital skills"
    - `workExperienceSection` → "Esperienze Lavorative" / "Work experiences"
    - `interestsSection` → "Interessi di ricerca e di lavoro" / "Work interests"
    - `publicationSection` → "Pubblicazioni" / "Publications"
    - `schoolSection` → "Scuole" / "Schools"
    - `conferencesSection` → "Conferenze" / "Conferences"
    - `languagesSection` → "Linguaggi" / "Languages"
    - `referencesSection` → "Riferimenti" / "References"

    These are wrapped in `Translate(ita=..., eng=...)` objects so the LaTeX template
    may choose the language dynamically.

    Use `set_language` to choose the language before running this (default is italian).

    Output
    ------
    None
        The rendered LaTeX content is written directly to `output_path`.

    Examples
    --------
    The body of the template embedded in the repo contains:

       <% if presentazione %>

       \section{<<presentationSection>>}
       << presentazione >>
       <% endif %>
       <% if digital_skills %>

       \section{<<digitalSkillsSection>>}
        <% for skill in digital_skills %>
       \cvitem{ << skill >> }{ << digital_skills[skill] >> }
        <% endfor %>
       <% endif %>
       <% if work_experience %>

       \section{<<workExperienceSection>>}
        <% for exp in work_experience%>
        << exp >>
        <% endfor %>
       <% endif %>

    You may call this function as:

        data = {
            "presentazione": "Hello...",
            "work_experience": [...],
            "digital_skills":skillDict([...]),
        }

        create_cv(data, "mytemplate.tex", "cv_output.tex")

    See the example in the repository, it will be easier ;)

    """

    # Load the LaTeX template
    with open(template, "r") as file:
        template_content = file.read()
    env = jinja2.Environment(
        block_start_string="<%",
        block_end_string="%>",
        variable_start_string="<<",
        variable_end_string=">>",
        comment_start_string="<#",
        comment_end_string="#>",
        trim_blocks=True,
        lstrip_blocks=True,
    )
    data = {
        "presentationSection": Translate(ita="Presentazione", eng="About me"),
        "educationSection": Translate(ita="Educazione", eng="Education"),
        "digitalSkillsSection": Translate(
            ita="Competenze digitali",
            eng="Digital skills",
        ),
        "workExperienceSection": Translate(
            ita="Esperienze Lavorative",
            eng="Work experiences",
        ),
        "interestsSection": Translate(
            ita="Interessi di ricerca e di lavoro",
            eng="Work interests",
        ),
        "publicationSection": Translate(ita="Pubblicazioni", eng="Publications"),
        "schoolSection": Translate(ita="Scuole", eng="Schools"),
        "conferencesSection": Translate(ita="Conferenze", eng="Conferences"),
        "languagesSection": Translate(ita="Linguaggi", eng="Languages"),
        "referencesSection": Translate(ita="Riferimenti", eng="References"),
    }
    data.update(datain)
    # Create a Jinja2 template
    template = env.from_string(template_content)

    # Render the template with the provided data
    rendered_content = template.render(
        data,
    )

    # Write the rendered content to the output file
    with open(output, "w") as file:
        file.write(rendered_content)
