import pandas as pd
students = {
    "Name":['Senses','ACE','Believe','HawletPackard'],
    "RollNo":[123098,123099,123100,123101],
    "Branch":['Robotics','Mechetronics','Digital Twining','Glass Making'],
    "City":['C_ABC','C_BCD','C_ACC','C_KLM']
}
print(students)
dframe = pd.DataFrame(students)
print(dframe)
print(dframe.shape)
print(dframe['Branch'])