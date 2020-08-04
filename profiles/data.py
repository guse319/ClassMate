schools = [
    'UAIS',
    'Home',
    'Other',
]

teacher_schools = [
    'UAIS',
]


tutor_schools = {
    'oakland.edu':'Oakland University',
    'umich.edu':'University of Michigan Ann Arbor',
}

subjects = [

    # Math
    'Algebra',
    'Geometry',
    'Calculus',
    'Math - Elementary',

    # History
    'APUSH',
    'WHAP',
    'History - Elementary',

    # English
    'Writing',
    'Reading',
    'Literature',
    'English - Elementary',

    # Science
    'Biology',
    'Chemistry',
    'Physics',
    'Science - Elementary',
]

queries = [
    'clients',
    'subjects',
    'accommodations',
]

def common(l1, l2):
    for i in l1:
        for j in l2:
            if i == j:
                return True
    return False
