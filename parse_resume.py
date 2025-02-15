import json

resume = {
    "personal_details": {
        "name": "Prithvi Chaudhary",
        "contact": {
            "email": "pr7852@srmist.edu.in",
            "phone": "+91 8800150468"
        }
    },
    "education": [
        {
            "degree": "Computer Science and Engineering",
            "institution": "SRM University",
            "location": "Chennai, TN",
            "year_of_completion": "2025",
            "cgpa": "9.21"
        },
        {
            "degree": "XII",
            "institution": "Modern Delhi Public School",
            "location": "Faridabad",
            "board": "CBSE",
            "year_of_completion": "2021",
            "percentage": "94.6%"
        },
        {
            "degree": "X",
            "institution": "Modern Delhi Public School",
            "location": "Faridabad",
            "board": "CBSE",
            "year_of_completion": "2019",
            "percentage": "91.6%"
        }
    ],
    "coursework": [
        "Database Management System",
        "Object Oriented Programming",
        "Programming in Python",
        "Computer Networking"
    ],
    "skills": {
        "programming": [
            "Python",
            "UI/UX",
            "Machine Learning",
            "C++",
            "MySQL",
            "HTML/CSS/JavaScript"
        ],
        "secondary": [
            "Logical Reasoning",
            "Good Orator",
            "Excel"
        ],
        "tools_applications": [
            "Visual Studio",
            "PyCharm",
            "Figma",
            "Scikit-Learn"
        ],
        "operating_systems": [
            "Windows",
            "macOS",
            "Linux"
        ]
    },
    "honors_awards": [
        "Organising committee of a 24-hour hackathon (Hacknova) - 2024",
        "Class Representative - 2021",
        "State Lego League Winner - 2017"
    ],
    "links": {
        "github": "Prithvi Chaudhary",
        "leetcode": "Prithvi Chaudhary",
        "linkedin": "Prithvi Chaudhary"
    },
    "experience": [
        {
            "job_title": "Python/Data Analysis Intern",
            "company": "EX Squared Solutions Pvt Ltd",
            "duration": "12 June 2023 – 12 July 2023",
            "location": "Faridabad, Haryana",
            "responsibilities": [
                "Automated data analysis tasks using Python, leveraging libraries like pandas, numpy, matplotlib, and scikit-learn.",
                "Conducted a weather analysis project, identifying outliers and visualizing temperature trends across cities, countries, and continents over a long period.",
                "Gained practical experience in handling large datasets and deriving actionable insights from complex data."
            ]
        }
    ],
    "volunteer_experience": [
        {
            "role": "Corporate Lead",
            "organization": "Newton School Coding Club",
            "location": "Coding club SRMIST",
            "responsibilities": [
                "Advanced logistics and technical initiatives within the club.",
                "Organized coding events, workshops, and competitions.",
                "Utilized coding skills and technical proficiency to facilitate club activities."
            ]
        },
        {
            "role": "Committee Member",
            "organization": "Aaruush",
            "event": "National level techno-management fest",
            "responsibilities": [
                "Orchestrated premier events, highlighting leadership and adept decision-making in the face of technical complexities."
            ]
        }
    ],
    "projects": [
        {
            "title": "Email Fetching Tool",
            "skills": ["Python", "IMAP"],
            "description": "Developed a Python tool to fetch Gmail emails from a specific user using IMAP, leveraging imaplib and email libraries. Implemented functions to extract email bodies, search for specific senders, and manage email labels."
        },
        {
            "title": "Traffic Analyzer",
            "skills": ["pandas", "matplotlib", "scikit-learn", "FBProphet"],
            "description": "Developed a traffic forecasting model for JetRail. Conducted time series analysis to predict traffic trends for the next 7 months. Provided data-driven insights to aid Unicorn Ventures in potential investment decisions."
        },
        {
            "title": "Emu Check",
            "description": "Part of Government Project - Railway EMU - Internet Of Things. Designed frontend. Detects any irregular behaviour using sensors and alarm immediately."
        }
    ],
    "certificates": [
        "Networking Essentials",
        "AWS Machine Learning Foundations",
        "AWS Cloud"
    ]
}

with open('resume.json', 'w') as f:
    json.dump(resume, f, indent=4)

print("Resume has been parsed and saved as resume.json")
