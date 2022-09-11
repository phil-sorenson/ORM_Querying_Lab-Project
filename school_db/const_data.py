

view_information = {
    '/lab/': {
        'problem_title': 'Example Solution',
        'supporting_documentation': [
            'https://docs.djangoproject.com/en/4.0/ref/models/querysets/#all'
        ],
        'expected_terminal_results': [
            'First Name: Jake Last Name: Sisko GPA: 4.0',
            'First Name: Keira Last Name: Nerys GPA: 3.5',
            'First Name: Julian Last Name: Bashir GPA: 4.4',
            'First Name: Molly Last Name: OBrien GPA: 3.0',
            'First Name: Keiko Last Name: Ishikawa GPA: 4.2',
            'First Name: Eli Last Name: Garak GPA: 3.0',
            'First Name: Thomas Last Name: Riker GPA: 2.5',
            'First Name: Michael Last Name: Eddington GPA: 3.7',
            'First Name: Beckett Last Name: Mariner GPA: 3.8',
            'First Name: Sam Last Name: Rutherford GPA: 2.0',
        ],
        'expected_resulting_sql': [
            {
                'query_number': 1,
                'query_lines': [
                    'SELECT `school_db_student`.`id`,',
                    '    `school_db_student`.`first_name`,',
                    '    `school_db_student`.`last_name`,',
                    '    `school_db_student`.`year`,',
                    '    `school_db_student`.`gpa`',
                    'FROM `school_db_student`',
                ]
            }
        ]
    },
    '/lab/one/': {
        'problem_title': 'Problem 1',
        'supporting_documentation': [
            'https://docs.djangoproject.com/en/4.0/ref/models/querysets/#filter',
            'https://docs.djangoproject.com/en/4.0/ref/models/querysets/#order-by',
        ],
        'expected_terminal_results': [
            'Full Name: Julian Bashir GPA: 4.4',
            'Full Name: Keiko Ishikawa GPA: 4.2',
            'Full Name: Jake Sisko GPA: 4.0',
            'Full Name: Beckett Mariner GPA: 3.8',
            'Full Name: Michael Eddington GPA: 3.7',
            'Full Name: Keira Nerys GPA: 3.5',
        ],
        'expected_resulting_sql': [
            {
                'query_number': 1,
                'query_lines': [
                    'SELECT `school_db_student`.`id`,',
                    '       `school_db_student`.`first_name`,',
                    '       `school_db_student`.`last_name`,',
                    '       `school_db_student`.`year`,',
                    '       `school_db_student`.`gpa`',
                    '  FROM `school_db_student`',
                    ' WHERE `school_db_student`.`gpa` > 3.0',
                    ' ORDER BY `school_db_student`.`gpa` DESC',
                ]
            }
        ]
    },
    '/lab/two/': {
        'problem_title': 'Problem 2',
        'supporting_documentation': [
            'https://docs.djangoproject.com/en/4.0/ref/models/querysets/#filter',
            'https://docs.djangoproject.com/en/4.0/ref/models/querysets/#year',
            'https://docs.djangoproject.com/en/4.0/ref/models/querysets/#lt',
        ],
        'expected_terminal_results': [
            'Full Name: Jackie Daytona',
            'Hire Date: 2001-10-10',
            ' ',
            'Full Name: Colin Robinson',
            'Hire Date: 2009-04-10',
            ' ',
            'Full Name: Guillermo de la Cruz',
            'Hire Date: 2009-11-18'
        ],
        'expected_resulting_sql': [
            {
                'query_number': 1,
                'query_lines': [
                    'SELECT `school_db_instructor`.`id`,',
                    '       `school_db_instructor`.`first_name`,',
                    '       `school_db_instructor`.`last_name`,',
                    '       `school_db_instructor`.`hire_date`',
                    '  FROM `school_db_instructor`',
                    ' WHERE `school_db_instructor`.`hire_date` < \'2010-01-01\''
                ]
            }
        ]
    },
    '/lab/three/': {
        'problem_title': 'Problem 3',
        'supporting_documentation': [
            'https://docs.djangoproject.com/en/4.0/ref/models/querysets/#get',
            'https://docs.djangoproject.com/en/4.0/ref/models/querysets/#filter',
        ],
        'expected_terminal_results': [
            'Instructor Name: Colin Robinson',
            'Courses:',
            '    - Science',
            '    - History'
        ],
        'expected_resulting_sql': [
            {
                'query_number': 1,
                'query_lines': [
                    'SELECT `school_db_instructor`.`id`,',
                    '       `school_db_instructor`.`first_name`,',
                    '       `school_db_instructor`.`last_name`,',
                    '       `school_db_instructor`.`hire_date`',
                    ' FROM `school_db_instructor`',
                    ' WHERE `school_db_instructor`.`id` = 2',
                    ' LIMIT 21'
                ]
            },
            {
                'query_number': 2,
                'query_lines': [
                    'SELECT `school_db_course`.`id`,',
                    '       `school_db_course`.`name`,',
                    '       `school_db_course`.`instructor_id`,',
                    '       `school_db_course`.`credits`',
                    ' FROM `school_db_course`',
                    ' WHERE `school_db_course`.`instructor_id` = 2'
                ]
            },
        ]
    },
    '/lab/four/': {
        'problem_title': 'Problem 4',
        'supporting_documentation': [
            'https://docs.djangoproject.com/en/4.0/ref/models/querysets/#count',
        ],
        'expected_terminal_results': [
            'Students Count: 10',
            'Courses Count: 10',
            'Instructors Count: 6'
        ],
        'expected_resulting_sql': [
            {
                'query_number': 1,
                'query_lines': [
                    'SELECT COUNT(*) AS `__count`',
                    '  FROM `school_db_student`'
                ]
            },
            {
                'query_number': 2,
                'query_lines': [
                    'SELECT COUNT(*) AS `__count`',
                    '  FROM `school_db_course`'
                ]
            },
            {
                'query_number': 3,
                'query_lines': [
                    'SELECT COUNT(*) AS `__count`',
                    '  FROM `school_db_instructor`'
                ]
            },
        ]
    },
    '/lab/five/': {
        'problem_title': 'Problem 5',
        'supporting_documentation': [
            'https://docs.djangoproject.com/en/4.0/ref/models/querysets/#create'
        ],
        'expected_terminal_results': [
            'Id: 11',
            'Full Name: Kyle Harwood',
            'Year: 2022',
            'GPA: 3.0'
        ],
        'expected_resulting_sql': [
            {
                'query_number': 1,
                'query_lines': [
                    'INSERT INTO `school_db_student` (`first_name`, `last_name`, `year`, `gpa`)',
                    'NOTE: The information in the values will be what you chose',
                    'VALUES (\'Kyle\', \'Harwood\', 2022, 3.0)'
                ]
            }
        ]
    },
    '/lab/six/': {
        'problem_title': 'Problem 6',
        'supporting_documentation': [
            'https://docs.djangoproject.com/en/4.0/ref/models/querysets/#update',
            'https://docs.djangoproject.com/en/4.0/ref/models/querysets/#get'
        ],
        'expected_terminal_results': [
            'Id: 11',
            'Full Name: Kyle Harwood',
            'GPA: 3.5'
        ],
        'expected_resulting_sql': [
            {
                'query_number': 1,
                'query_lines': [
                    'UPDATE `school_db_student`',
                    'NOTE: The gpa value will be what you chose',
                    '   SET `gpa` = 3.5',
                    ' WHERE `school_db_student`.`id` = 11'
                ]
            },
            {
                'query_number': 2,
                'query_lines': [
                    'SELECT `school_db_student`.`id`,',
                    '    `school_db_student`.`first_name`,',
                    '    `school_db_student`.`last_name`,',
                    '    `school_db_student`.`year`,',
                    '    `school_db_student`.`gpa`',
                    'FROM `school_db_student`',
                    'WHERE `school_db_student`.`id` = 11',
                    'LIMIT 21'
                ]
            }
        ]
    },
    '/lab/seven/': {
        'problem_title': 'Problem 7',
        'supporting_documentation': [
            'https://docs.djangoproject.com/en/4.0/ref/models/querysets/#delete'
        ],
        'expected_terminal_results': [
            'Great! It failed and couldnt find the object because we deleted it!'
        ],
        'expected_resulting_sql': [
            {
                'query_number': 1,
                'query_lines': [
                    'SELECT `school_db_student`.`id`,',
                    '       `school_db_student`.`first_name`,',
                    '       `school_db_student`.`last_name`,',
                    '       `school_db_student`.`year`,',
                    '       `school_db_student`.`gpa`',
                    '  FROM `school_db_student`',
                    ' WHERE `school_db_student`.`id` = 15'
                ]
            },
            {
                'query_number': 2,
                'query_lines': [
                    ' DELETE',
                    '  FROM `school_db_studentcourse`',
                    ' WHERE `school_db_studentcourse`.`student_id` IN (15)'
                ]
            },
            {
                'query_number': 3,
                'query_lines': [
                    'NOTE this query is included in the starter code. See the query in the try catch',
                    'SELECT `school_db_student`.`id`,',
                    '       `school_db_student`.`first_name`,',
                    '       `school_db_student`.`last_name`,',
                    '       `school_db_student`.`year`,',
                    '       `school_db_student`.`gpa`',
                    '  FROM `school_db_student`',
                    ' WHERE `school_db_student`.`id` = 15',
                    ' LIMIT 21'
                ]
            },
        ]
    },
    '/lab/bonus/': {
        'problem_title': 'Bonus Problem',
        'supporting_documentation': [
            'https://docs.djangoproject.com/en/4.0/topics/db/aggregation/',
            'https://docs.djangoproject.com/en/4.0/ref/models/querysets/#annotate',
            'https://docs.djangoproject.com/en/4.0/ref/models/querysets/#filter',
            'https://docs.djangoproject.com/en/4.0/ref/models/querysets/#count'
        ],
        'expected_terminal_results': [
            'Instructor Name: Guillermo de la Cruz',
            'Instructor Name: Brad Baskshi'
        ],
        'expected_resulting_sql': [
            {
                'query_number': 1,
                'query_lines': [
                    'SELECT `school_db_instructor`.`id`,',
                    '       `school_db_instructor`.`first_name`,',
                    '       `school_db_instructor`.`last_name`,',
                    '       `school_db_instructor`.`hire_date`,',
                    '       COUNT(`school_db_course`.`id`) AS `course__count`',
                    '  FROM `school_db_instructor`',
                    '  LEFT OUTER JOIN `school_db_course`',
                    '    ON (`school_db_instructor`.`id` = `school_db_course`.`instructor_id`)',
                    ' GROUP BY `school_db_instructor`.`id`',
                    'HAVING COUNT(`school_db_course`.`id`) = 1',
                    ' ORDER BY NULL'
                ]
            }
        ]
    },
}
