from cvcompiler import (
    Education,
    workExperience,
    create_cv,
    Translate,
    Skill,
    SkillSet,
    skillDict,
    Conference,
    Talk,
    Poster,
    Presentation,
    Languages,
    Language,
    set_language,
    make_cover_letter,
)

presentation = Presentation(
    Translate(
        ita="""Nato fisico, cresciuto sviluppatore/ingegnere del software.


Il mio ruolo attuale è convincere parte del codice di PLUMED a funzionare su una GPU. In passato ho scritto programmi scientifici per i laboratori in cui ho studiato/lavorato e sono sempre stato attento a lasciare un codice ben documentato e facile da usare per i futuri colleghi.

In un certo senso il mio lavoro è sempre stato lavorare con interfacce o di "traduzione":

 - La fisica come scienza cerca di mettere in comunicazione uomo e natura, usando la matematica come linguaggio
 - ho portato da Fortran a C++ un codice di ottimizzazione globale, che poi ho interfacciato con QuantumEspresso
 - ho cercato di fittare un potenziale di interazione tra Au e S
 - ho interfacciato dottorandi (che in genere non leggono mai manuali) con codici scientifici
 - ho aiutato a migliorare un interfaccia tra PLUMED e Python
 - sto "portando" parte del codice di PLUMED su GPU.

Sono principalmente uno sviluppatore C++, ho un rapporto "interessato" con Python. E so impostare script in bash anche abbastanza complessi. So muovermi in progetti che si compilano passando per CMake o GNUAutotools.
""",
        eng="""I am a Physicist by education, software developer/engineer by vocation.

My current role is to convince some component of PLUMED to run on the GPU, at SISSA. Previously, I helped keep in order (and well documented) the internal script libraries of my laboratories.

My job was always in translating or in interfaces:

 - Physics is the science that makes nature understandable by human beings by using math as a language
 - I ported a global optimization program from Fortran to C++
 - I tried to fit a potential to describe the Au -- S interface in nanoparticles
 - I interfaced real PhD students (that by definition NEVER read manuals) with atomic structure analysis python packages
 - Now I am translating part of the PLUMED code to run it on the GPU
 - I also helped make it possible to call a Python script with an embedded (in PLUMED) Python interpreter by a PLUMED instance that runs within a Python interpreter

I am primarily a **C++** developer, I have a *love-hate* relationship with **Python**, and I do like setting up bash scripts (I can use arrays!). I am familiar with CMake and with writing Makefiles, and I also have the basis to interact with GNUAutotools.
""",
    )
)

####WORK EXPERIENCES
plumedDeveloper = workExperience(
    Translate(
        ita="Tecnologo di Ricerca - Sviluppatore di PLUMED",
        eng="Research technologist -- PLUMED developer",
    ),
    "16/04/2023",
    "ongoing",
    employer="Scuola Internazionale Superiore di Studi Avanzati (SISSA)",
    city="Trieste, Italia",
    description=Translate(
        ita=r""" -  Manutenzione e miglioramento del programma open source PLUMED (**C++**, **GNU autotools**, **Python**, **GitHub Workflows**)
 -  Manutenzione integrazione continua e test (**GitHub Workflows**)
 -  Contributo ad interfaccia PLUMED-Python (**pybind11**, **pip**, **CMake**, **scikit\_build\_core**)
 -  Accelerazione di alcune componenti di PLUMED con GPU (**CUDA**, **openACC**).
 -  Manutenzione siti di supporto per PLUMED (**Python**, **GitHub Workflows**, Markdown)""",
        eng=""" - Maintenance and developing of the open source program PLUMED (C++, GNU autotools, Python, GitHub Workflows)
 - Maintenance CI and tests (**GitHub Workflows**)
 - Contribution to the PLUMED-Python interface (**pybind11**, **pip**, **CMake**, **scikit\_build\_core**)
 - Acceleration of some components in PLUMED con GPU (**CUDA**, **openACC**).
 - Maintenance of support sites for PLUMED (**Python**, **GitHub Workflows**, Markdown)""",
    ),
)
postDocInTurin = workExperience(
    Translate(ita="Assegno di ricerca", eng="Post-doc research grant"),
    "01/09/2021",
    "15/04/2023",
    employer="Politecnico di Torino",
    city="Torino, Italia",
    description=Translate(
        ita=r""" -  Simulazione e analisi traiettorie di nanoparticelle metalliche
 -  Gestione risorse computazionali interne al laboratorio
 -  Manutenzione programmi interni al laboratorio (**Bash** , **Python 3**).

**In particolare ho imparato a gestire un pacchetto python su GitHub e a pubblicarlo su PyPI tramite GitHub workflow**

**Ho anche iniziato ad applicare tecniche di integrazione continua** (test e validazione di codice)
""",
        eng=r""" - Simulation and trajectory analysis of metallic nanoparticles
 - Maintenance and software organization of computational resources of the laboratory
 - Maintenance internal software tools (Bash , Python 3).

**In particular I learned setting up and maintainig a python package on GitHub, and to publish it on PyPi via a GitHub workflow.**

**I also started using and mastering the CI/CD workflow for testing and validating the code.**
""",
    ),
)
postDocInGenova = workExperience(
    Translate("Borsa DR", "Borsa DR [research grant]"),
    "01/02/2021",
    "31/07/2021",
    employer="Università degli studi di Genova",
    city="Genova, Italia",
    description=Translate(
        ita=r"""Continuazione e finalizzazione del lavoro fatto durante il dottorato:

 -  Studio potenziale atomistico di interazione tra zolfo in tioli e superfici di oro a partire da calcoli e dati DFT
(Density Functional Theory).
 -  **Manutenzione programmi interni al laboratorio** (**C++**, Bash , Python 2.7 e 3)""",
        eng="""Finalization of my doctorate work:

 - Developing an atomistic interaction potenzial between sulphur in thiols and gold sufaces from data generated with DFT (Density Functional Theory) calculations.
 - Mainteinance of internal tools (**C++**, Bash , Python 2.7 e 3)
""",
    ),
)
###EDUCATION (Titles)
phd = Education(
    "Ph.D. in Material Science",
    "31/10/2017",
    "31/12/2020",
    "Università degli studi di Genova",
    "Genova, Italia",  # | Campi di studio: Scienza dei Materiali | Livello EQF: Livello 8 EQF | Tesi:
    grade=None,
    field=Translate("Scienza dei Materiali", "Materials Science"),
    eqf=8,
    title=Translate(
        ita=r"Computational approaches to the study of the electronic properties, structure and functionalization of metal nanoparticles [Approcci computazionali allo studio delle proprietà elettroniche, della struttura e della funzionalizzazione di nanoparticelle metalliche.]",
        eng="Computational approaches to the study of the electronic properties, structure and functionalization of metal nanoparticles",
    ),
    description=Translate(
        ita=r""" -  Definizione e studio potenziale atomistico di interazione tra zolfo in tioli e superfici di oro a partire da calcoli e dati DFT (Density Functional Theory).
 - Scrittura programma di best fit in C++ e OpenCL utilizzando l’algoritmo Particle Swarm Optimization
 - Implementazione del potenziale Au-S in LAMMPS.
 - Manutenzione programmi interni al laboratorio (**C++**, Bash , Python 2.7 e 3).
""",
        eng=r""" -  Definition and study of an atomistic interaction potential between the sulphur in a thiolate and golden surfaces, starting from data and calculations made with the DFT (Density Functional Theory).
 - I wrote a best fit program in **C++** and **OpenCL** using the Particle Swarm Optimization algorithm
 - I implemented the Au-S potenzial in LAMMPS
 - I contributed to the minteinance of the internal lab programs (**C++**, Bash , Python 2.7 e 3).

""",
    ),
)
masterthesis = Education(
    "Laurea Magistrale",
    "2012",
    "25/10/2017",
    "Università degli studi di Genova",
    "Genova, Italia",
    field="Fisica della Materia",
    grade="109/110",
    eqf=7,
    title=Translate(
        ita=r"""Density Functional Theory (DFT) global optimization of metal clusters [Ottimizzazione globale di cluster metallici tramite l’utilizzo della teoria del funzionale densità (DFT)]""",
        eng="Density Functional Theory (DFT) global optimization of metal clusters",
    ),
    description=Translate(
        ita=r""" -  Riscrittura da Fortran a C++ del programma di Basin Hopping (BH++) del gruppo di ricerca
 -  Creazione interfaccia tra QUANTUM Espresso e BH++
 -  Validazione e utilizzo di BH++ e dell’interfaccia BH++-QE su nanocluster di AuAg di 38 e 55 atomi
""",
        eng=r""" - I rewrote the Basin Hopping (BH++) program of the laboratory from Fortran to C++
 - I set up an interface between BH++ and QUANTUM Espresso(QE)
 - I validated and used the BH++-QE interface on nanocluster of AuAg of 38 and 55 atoms.
""",
    ),
)
bachelor = Education(
    "Laurea Triennale",
    "2009",
    "25/03/2014",
    "Università degli studi di Genova",
    "Genova, Italia",
    grade="102/110",
    field=Translate("Fisica Sperimentale", "Experimental Physics"),
    eqf=6,
    title=Translate(
        ita="L'effetto tunnel e il decadimento alfa",
        eng="L'effetto tunnel e il decadimento alfa[Tunnel effect and alpha decay]",
    ),
)


#####skills


crosslanguage = SkillSet(
    "Cross-Language",
    Skill("Object Oriented Program (OOP)"),
    Skill("Design patterns"),
    Skill("OpenACC"),
    Skill("OpenMP"),
    Skill("Functional Programming"),
)
computerLanguages = SkillSet(
    "Programming and Scripting Languages",
    Skill("C++", emph=True),
    Skill("Bash"),
    Skill("CUDA", emph=True),
    Skill("OpenCL"),
    Skill("LaTeX"),
    Skill("AWK"),
    Skill("Javascript"),
)
scientificSoftware = SkillSet(
    "Software scientifici",
    Skill("CP2K"),
    Skill("LAMMPS"),
    Skill("Quantum ESPRESSO"),
    Skill("MATLAB"),
    Skill("Plumed"),
    Skill("Wolfram Mathematica"),
)
software = SkillSet(
    "Software",
    Skill("Microsoft Office"),
    Skill("Open Office"),
    Skill("make"),
    Skill("GNU Autotools"),
    Skill("CMake"),
    Skill("Git"),
    Skill("enviroment modules"),
    Skill("Github, Github actions", emph=True),
    Skill("gnuplot"),
)
IDEs = SkillSet(
    "IDE e editor testuali",
    Skill("vscode"),
    Skill("Neovim"),
)


# conferences
icsc25 = Conference(
    date="12/05/2025 - 14/05/2025",
    place="Trieste, Italia",
    title="National Conference of ICSC Spoke 7: MATERALS & MOLECULAR SCIENCES",
    contribution=Talk(
        Translate(
            ita="Bringing PLUMED to the GPU: implementing a flexible parallelization interface for a community developed code [Portare PLUMED sulla GPU: implementazione di un'interfaccia di parallelizzazione flessibile per un codice aperto]",
            eng="Bringing PLUMED to the GPU: implementing a flexible parallelization interface for a community developed code",
        ),
        invited=True,
    ),
)

acbd19 = Conference(
    date="21/10/2019 - 25/10/2019",
    place="Okinawa, Giappone",
    title="ACBD Advances in Cluster Beam Deposition",
    contribution=Poster(
        Translate(
            ita="Development of a new Au-S classical potential for the simulation of nanoparticle-bio interactions [Sviluppo di un nuovo potenziale classico Au-S per simulazione di interazioni nanoparticelle-bio]",
            eng="Development of a new Au-S classical potential for the simulation of nanoparticle-bio interactions",
        )
    ),
)

grc19 = Conference(
    date="15/06/2019 - 20/06/2019",
    place="Les Diablerets, Svizzera",
    title="GRC Clusters and Nanostructures",
    contribution=Poster(
        Translate(
            ita="A Gold-Sulphur Atomistic Potential For Molecular Dynamics [Un potenziale oro–zolfo per la dinamica molecolare]",
            eng="A Gold-Sulphur Atomistic Potential For Molecular Dynamics",
        )
    ),
)

grs19 = Conference(
    date="14/06/2019 - 15/06/2019",
    place="Les Diablerets, Svizzera",
    title="GRS Clusters and Nanostructures",
    contribution=Poster(
        Translate(
            ita="A Gold-Sulphur Atomistic Potential For Molecular Dynamics [Un potenziale oro–zolfo per la dinamica molecolare]",
            eng="A Gold-Sulphur Atomistic Potential For Molecular Dynamics",
        )
    ),
)

imn19 = Conference(
    date="03/06/2019 - 06/06/2019",
    place="Genova, Italia",
    title="IMN 2019 International Meeting on Nanoalloys",
    contribution=[
        Talk(
            Translate(
                ita="A New Basin Hopping Suite For Multi-Component Nanoparticles [Una nuova suite per il Basin Hopping di nanoparticelle multicomponenti]",
                eng="A New Basin Hopping Suite For Multi-Component Nanoparticles",
            )
        ),
        Poster(
            Translate(
                ita="A Gold-Sulphur Atomistic Potential For Molecular Dynamics [Un potenziale oro--zolfo per la dinamica molecolare]",
                eng="A Gold-Sulphur Atomistic Potential For Molecular Dynamics",
            )
        ),
    ],
    note=Translate(
        ita="Ho contributo all’organizzazione della conferenza",
        eng="I contribuited to the organization of the conference",
    ),
)

imn18 = Conference(
    date="21/05/2018 - 24/05/2018",
    place="Orléans, Francia",
    title="IMN 2018 International Meeting on Nanoalloys",
    contribution=Poster(
        Translate(
            ita="Conflicting behaviour for Au impurities in Ag nanoclusters [Comportamenti anomali di impurità di Au in nanocluster di Ag]",
            eng="Conflicting behaviour for Au impurities in Ag nanoclusters",
        )
    ),
)


languages = Languages(
    mother_tongues=Translate("Italiano", "Italian"),
    other_languages=Language(
        Translate("Inglese", "English"),
        listening="B1",
        reading="B2",
        writing="B1",
        spoken_production="B1",
        spoken_interaction="B2",
    ),
)


if __name__ == "__main__":
    from sys import argv

    lang = "ita"
    if len(argv) > 1:
        lang = argv[1]

    set_language(lang)

    # Example data to populate the CV
    with open("private.json", "r") as pf:
        import json

        private = json.load(pf)
        assert "address" in private, '"address" should be in "private.json"'
        assert "address_country" in private, (
            '"address_country" should be in "private.json"'
        )
        assert "mobile" in private, '"mobile" should be in "private.json"'
    cv_data = {
        # am not using update here to be sure that
        "address": private["address"],
        "address_country": private["address_country"],
        "mobile": private["mobile"],
        # You can choose the photo from here, no need for adding the extension
        "photo": "Photo_small",
        # "photo": "Photo",
        # custom data:
        "presentazione": presentation,
        "work_experience": [
            plumedDeveloper,
            postDocInTurin,
            postDocInGenova,
        ],
        "education": [
            phd,
            masterthesis,
            bachelor,
        ],
        "digital_skills": skillDict(
            crosslanguage,
            computerLanguages,
            scientificSoftware,
            software,
            IDEs,
        ),
        "languages": languages,
        "bibliography": "yes",
        "conferences": [
            icsc25,
            acbd19,
            grc19,
            grs19,
            imn19,
            imn18,
        ],
        "privacy_disclaimer": "yes",
    }
    if "cover_letter" in private:
        cv_data["cover_letter"] = make_cover_letter(private["cover_letter"])
    create_cv(
        cv_data,
        template="cvtemplate.tex",
        output=f"cv_{lang}.tex",
    )
