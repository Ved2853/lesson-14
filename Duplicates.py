student_data = {'id1':
        {'name': ['Ved'],
        'class': ['IX'],
        'subject_integration': ['Maths, Phisics, Biology']
         },
        'id2':
        {'name': ['Veer'],
         'class': ['IX'],
         'subject_integration': ['Maths, Phisics, Biology']
         },
         'id3':
         {'name': ['Abhishek'],
           'class': ['IX'],
          'subject_integration': ['Maths, Phisics, Biology']
          },
          'id4':
         {'name': ['Ved'],
          'class': ['IX'],
         'subject_integration': ['Maths, Phisics, Biology']
         },
}

result = {}

for key,value in student_data.items():
    if value not in result.values():
        result[key] = value

print(result)