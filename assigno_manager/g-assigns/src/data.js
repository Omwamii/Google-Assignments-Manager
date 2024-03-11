const units =  [
    {
        "id": "640286398164",
        "name": "Group1_CSC_319_October2023_Feb2024"
    },
    {
        "id": "634082930362",
        "name": "CSC315 Distributed Systems, 2023-2024"
    },
    {
        "id": "632230740983",
        "name": "CSC311G1-G2-YR2023-2024 ANALYSIS AND DESIGN OF ALGORTHMS"
    },
    {
        "id": "632004324252",
        "name": "Computer Graphics CSC314"
    },
    {
        "id": "631842527791",
        "name": "CSC 316 Introduction to organizations and management"
    },
    {
        "id": "346224049561",
        "name": "CSC 318 - 2023/2024"
    },
    {
        "id": "596386506857",
        "name": "CSC228 Web and Services Programming Year 2023"
    },
    {
        "id": "594715479420",
        "name": "2023_CSC229 ML Algorithms and Programming"
    }
];

const grades = [
    {
        "id": "641897503732",
        "title": "Assignment 6: MATLAB OnRamp",
        "link": "https://classroom.google.com/c/NjMyMDA0MzI0MjUy/a/NjQxODk3NTAzNzMy/details",
        "maxPoints": 20,
        "grade": 20
    },
    {
        "id": "641698591232",
        "title": "Assignment 5: Plot a Polygon using MATLAB",
        "link": "https://classroom.google.com/c/NjMyMDA0MzI0MjUy/a/NjQxNjk4NTkxMjMy/details",
        "maxPoints": 10,
        "grade": 7
    },
    {
        "id": "643034694194",
        "title": "Project Proposal Ideation in PPT format",
        "link": "https://classroom.google.com/c/NjMyMDA0MzI0MjUy/a/NjQzMDM0Njk0MTk0/details",
        "maxPoints": 25,
        "grade": 16
    },
    {
        "id": "635102608329",
        "title": "Assignment 1",
        "link": "https://classroom.google.com/c/NjMyMDA0MzI0MjUy/a/NjM1MTAyNjA4MzI5/details",
        "maxPoints": 10,
        "grade": 8
    },
    {
        "id": "654918167178",
        "title": "Project Animation Presentation and Project Documentation",
        "link": "https://classroom.google.com/c/NjMyMDA0MzI0MjUy/a/NjU0OTE4MTY3MTc4/details",
        "maxPoints": 30,
        "grade": 17
    },
    {
        "id": "637563411260",
        "title": "Assignment 3: Transformations ",
        "link": "https://classroom.google.com/c/NjMyMDA0MzI0MjUy/a/NjM3NTYzNDExMjYw/details",
        "maxPoints": 10,
        "grade": 0
    },
    {
        "id": "637862764624",
        "title": "Assignment 4: Introduction to MATLAB: What is MATLAB?",
        "link": "https://classroom.google.com/c/NjMyMDA0MzI0MjUy/a/NjM3ODYyNzY0NjI0/details",
        "maxPoints": 25,
        "grade": 19
    },
    {
        "id": "635098307230",
        "title": "Rendering a Doughnut/Kettle in Blender",
        "link": "https://classroom.google.com/c/NjMyMDA0MzI0MjUy/a/NjM1MDk4MzA3MjMw/details",
        "maxPoints": 25,
        "grade": 15
    }
]

const pendingWork = 
[
    {
        "id": "657274133578",
        "unit": "CSC315 Distributed Systems, 2023-2024",
        "title": "RPC assignment ",
        "classLink": "https://classroom.google.com/c/NjM0MDgyOTMwMzYy/a/NjU3Mjc0MTMzNTc4/details",
        "points": 100,
        "dueTime": " No due time",
        "courseId": "634082930362"
    },
    {
        "id": "642584519816",
        "unit": "CSC 318 - 2023/2024",
        "title": "LAB 4",
        "classLink": "https://classroom.google.com/c/MzQ2MjI0MDQ5NTYx/a/NjQyNTg0NTE5ODE2/details",
        "points": 100,
        "dueTime": " No due time",
        "courseId": "346224049561"
    },
    {
        "id": "553588644847",
        "unit": "CSC228 Web and Services Programming Year 2023",
        "title": "SOA Practice",
        "classLink": "https://classroom.google.com/c/NTk2Mzg2NTA2ODU3/a/NTUzNTg4NjQ0ODQ3/details",
        "points": 100,
        "dueTime": " No due time",
        "courseId": "596386506857"
    },
    {
        "id": "603550220616",
        "unit": "CSC228 Web and Services Programming Year 2023",
        "title": "RESTful API web service Programming Practice - Use PHP, Python, Java or Nodejs",
        "classLink": "https://classroom.google.com/c/NTk2Mzg2NTA2ODU3/a/NjAzNTUwMjIwNjE2/details",
        "points": 100,
        "dueTime": " No due time",
        "courseId": "596386506857"
    },
    {
        "id": "596386506874",
        "unit": "CSC228 Web and Services Programming Year 2023",
        "title": "CSC 228 Web Assignment 1- HTML and CSS Practice 18/02/2022",
        "classLink": "https://classroom.google.com/c/NTk2Mzg2NTA2ODU3/a/NTk2Mzg2NTA2ODc0/details",
        "points": 15,
        "dueTime": " No due time",
        "courseId": "596386506857"
    },
    {
        "id": "596386506883",
        "unit": "CSC228 Web and Services Programming Year 2023",
        "title": "CSC 228 Continuous Assessment Special",
        "classLink": "https://classroom.google.com/c/NTk2Mzg2NTA2ODU3/a/NTk2Mzg2NTA2ODgz/details",
        "points": 50,
        "dueTime": " No due time",
        "courseId": "596386506857"
    },
    {
        "id": "606513715548",
        "unit": "2023_CSC229 ML Algorithms and Programming",
        "title": "Self Study on Feature Selection and Extraction",
        "classLink": "https://classroom.google.com/c/NTk0NzE1NDc5NDIw/a/NjA2NTEzNzE1NTQ4/details",
        "points": null,
        "dueTime": " No due time",
        "courseId": "594715479420"
    },
    {
        "id": "587581870646",
        "unit": "CSC 224 (Oct 2022 - Feb 2023)",
        "title": "Final Assignment",
        "classLink": "https://classroom.google.com/c/NTg3NTgwOTExMzkz/a/NTg3NTgxODcwNjQ2/details",
        "points": 100,
        "dueTime": " No due time",
        "courseId": "587580911393"
    }
];

const currentWork = 
{
    "id": "641698591232",
    "courseId": "632004324252",
    "title": "Assignment 5: Plot a Polygon using MATLAB",
    "description": "By using MATLAB;\n\n1. Plot a polygon named t with coordinates;  (8,7) (12,28) (34,28) (63,7)\nPerform the following translations on t\n \n2. Translate t by (-20,2). Name the resultant polygon t1\n3. Scale t by a factor of 2. Name the resultant polygon t2\n4. Scale t by (2,1). Name the resultant polygon t3\n5. Rotate t by 30 degrees about the origin. Name the resultant polygon t4\n6.  Rotate t by 45 degrees about the point (23,7). Name the resultant polygon t5\n7. Use the rotate command on t and plot the output. Animate the effect.\n\nN/B: Label all the graphs by the title of the transformation e.g “Rotation by 30 degrees about the origin” Plot all resultant polygons alongside the original polygon(t)",
    "maxPoints": 10,
    "time": "Deadline passed by 5 days, 14 hrs, 15 minutes"
};

const notifs = 
    [
        {
            "id": "661533168009",
            "courseId": "632004324252",
            "text": "Please resubmit assignment 5 on Google Classroom. \nFor Assignment on Project Ideation PPT - only the team leader to resubmit the team's PPT\n presentation. \nThis two assignments will be open tomorrow until 5 pm",
            "time": "35 days ago"
        },
        {
            "id": "628532100904",
            "courseId": "632004324252",
            "text": "Where did you guys submit assignments 5 and 6 and your project proposal ideation?  ",
            "time": "35 days ago"
        },
        {
            "id": "658419921582",
            "courseId": "632004324252",
            "text": "Good Morning Class. Your Exam is on Monday the 5th  of February from 2 pm-4:30 pm. Kindly do not bring your phones to the exam room and bring your calculator no sharing of calculators.  Below find a study guide: \n\nUnderstand foundational concepts in Computer Graphics.\nFocus on understanding and comparing different line drawing algorithms, particularly the DDA and Bresenham algorithm\nLearn about raster and vector scan displays and performance calculations.\nStudy how 3D scenes are rendered onto 2D displays and the techniques used for texture mapping.\nDive into homogenous coordinates and the matrix representations for basic transformations like translation, scaling, and rotation.\n Understand modeling and rendering, and study line clipping algorithms.\nUnderstand terms related to colour representation. ",
            "time": "39 days ago"
        },
        {
            "id": "657501928385",
            "courseId": "632004324252",
            "text": "Good Morning class, the Project presentations will be in the MSC lab starting at 9 am.\nYou should be able to do a PPT of your Project and then show the animation. The PPT and project report should be uploaded by now on Google Classroom.\n\n",
            "time": "45 days ago"
        },
        {
            "id": "657022118160",
            "courseId": "632004324252",
            "text": "There is a physical class today ",
            "time": "47 days ago"
        },
        {
            "id": "656692748596",
            "courseId": "632004324252",
            "text": "The presentations will be done on Thursday from 9 am for both group 1 and group 2. The venue will be determined closer to the date. Kindly upload your reports as soon as possible. The deadline is Wednesday the 23rd of January.",
            "time": "48 days ago"
        },
        {
            "id": "639135890813",
            "courseId": "632004324252",
            "text": "Good Morning, class, today will be online. https://meet.google.com/ite-vtjn-mir",
            "time": "87 days ago"
        },
        {
            "id": "644904507157",
            "courseId": "632004324252",
            "text": "Let me iterate, the proposal submitted needs to be in Microsoft Word for me to check for plagiarism. ",
            "time": "94 days ago"
        }
    ];

const submissions = [
    {
        "id": "Cg4I7dOBwIsKEMq43cSQEw",
        "title": "RPC assignment ",
        "link": "https://classroom.google.com/c/NjM0MDgyOTMwMzYy/a/NjU3Mjc0MTMzNTc4/details",
        "maxPoints": 100,
        "grade": null,
        "submission": {
            "attachments": [
                {
                    "driveFile": {
                        "id": "1AJd8pCzb6pp6WtzXkKREOThQzrU_U6AM",
                        "title": "client.py",
                        "alternateLink": "https://drive.google.com/file/d/1AJd8pCzb6pp6WtzXkKREOThQzrU_U6AM/view?usp=drive_web"
                    }
                },
                {
                    "driveFile": {
                        "id": "1U1BcMCbtNaxYwv2OxOr5lO8xY5C3Gh0o",
                        "title": "server.py",
                        "alternateLink": "https://drive.google.com/file/d/1U1BcMCbtNaxYwv2OxOr5lO8xY5C3Gh0o/view?usp=drive_web"
                    }
                }
            ]
        }
    },
    {
        "id": "Cg4I7dOBwIsKENyBhubbEg",
        "title": "Logical clocks",
        "link": "https://classroom.google.com/c/NjM0MDgyOTMwMzYy/a/NjQzMTE2OTI1MTQ4/details",
        "maxPoints": 100,
        "grade": null,
        "submission": {
            "attachments": [
                {
                    "driveFile": {
                        "id": "1nG8kUWY0QfnAQ_icAmssi85DZoNF-Vis",
                        "title": "socket_clocks.py",
                        "alternateLink": "https://drive.google.com/file/d/1nG8kUWY0QfnAQ_icAmssi85DZoNF-Vis/view?usp=drive_web"
                    }
                }
            ]
        }
    },
    {
        "id": "Cg4I7dOBwIsKEP-gpf_PEg",
        "title": "Gossip algorithm assignment (Group 1&2)",
        "link": "https://classroom.google.com/c/NjM0MDgyOTMwMzYy/a/NjM5OTQ4NjQwMzgz/details",
        "maxPoints": 100,
        "grade": null,
        "submission": {
            "attachments": [
                {
                    "driveFile": {
                        "id": "1h5CwA9rKNaTkVth0OwWQE32P9j4Dz_lG",
                        "title": "gossip.py",
                        "alternateLink": "https://drive.google.com/file/d/1h5CwA9rKNaTkVth0OwWQE32P9j4Dz_lG/view?usp=drive_web"
                    }
                }
            ]
        }
    },
    {
        "id": "Cg4I7dOBwIsKEK6Mx5K6Eg",
        "title": "Group 2, Hadoop",
        "link": "https://classroom.google.com/c/NjM0MDgyOTMwMzYy/a/NjM0MDgzNDYwNjU0/details",
        "maxPoints": 100,
        "grade": null,
        "submission": {
            "attachments": [
                {
                    "driveFile": {
                        "id": "1sWhhntzzVLXGiX2bk9LHGYnb50DvJTBatIiP-CEZC5w",
                        "title": "Hadoop overview",
                        "alternateLink": "https://docs.google.com/document/d/1sWhhntzzVLXGiX2bk9LHGYnb50DvJTBatIiP-CEZC5w/edit?usp=drive_web",
                        "thumbnailUrl": "https://lh3.google.com/drive-storage/AJQWtBMpRPxlU-a0QJryfhUqaAuW0limlfBeuSggat61iDBYFg9QX62aF5WUPt6_eG-UQwmen0mL1uqqxaRYOdltdgksUvO314HZRUrgwxbycG8omdncAWxVLcP3aqoD8iGpCg=s200"
                    }
                }
            ]
        }
    },
    {
        "id": "Cg4I7dOBwIsKENfx1PXJEg",
        "title": "Socket communication",
        "link": "https://classroom.google.com/c/NjM0MDgyOTMwMzYy/a/NjM4MzE3ODM2NTAz/details",
        "maxPoints": 100,
        "grade": null,
        "submission": {
            "attachments": [
                {
                    "driveFile": {
                        "id": "1sp-sWgFXL6HnuIlBPlQxbAw94dL_9gIA",
                        "title": "socket_server.py",
                        "alternateLink": "https://drive.google.com/file/d/1sp-sWgFXL6HnuIlBPlQxbAw94dL_9gIA/view?usp=drive_web"
                    }
                },
                {
                    "driveFile": {
                        "id": "1-5Dpa2UxiHCJuIPzgG13mV1fCTeZNWXg",
                        "title": "socket_client.py",
                        "alternateLink": "https://drive.google.com/file/d/1-5Dpa2UxiHCJuIPzgG13mV1fCTeZNWXg/view?usp=drive_web"
                    }
                }
            ]
        }
    }
]

const stats = {
        "CSC_319": 80,
        "CSC315": 75,
        "CSC311": 74,
        "CSC314": 85,
        "CSC 316": 65,
        "CSC 318": 68,
        "CSC228": 34,
        "2023": 45,
        'more': 87,
        "even": 97
}
export  { units, currentWork, pendingWork, grades, notifs, submissions, stats }