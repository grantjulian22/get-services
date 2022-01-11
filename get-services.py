import subprocess
import csv

# this is a script to list out all services used by each project in an organization for GCP
# it uses bash commands

# name of the output file
OUTPUT_FILE_NAME = 'my-output.csv'

# directly below is a bash command to log into correct GCP org
# you can uncomment this if you want this script to log you into gcloud every time it runs. 
# It requires user input so it can be kind of annoying (which is why its commented out)

'''
bashCommand = "gcloud auth login"
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
print(output)
print(error)
'''

# bash command to fetch all projects in GCP org and store into output variable
bashCommand = "gcloud projects list --format=value[separator=','](projectId)"
print(bashCommand)
process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

# seperate projects into a list based on the newline character '\n'
if type(output) == type(b''): output = output.decode('ascii')
output = output.split('\n')
print("assessing a total of " + str(len(output)) + " projects")

# loop through all projects, run command to get services, and write to CSV file
# this will write to whatever file is specified in OUTPUT_FILE_NAME
with open(OUTPUT_FILE_NAME, 'w') as file:

    writer = csv.writer(file)
    writer.writerow(['project name', 'services'])

    # loop through every project
    for i in range(len(output)):

        bashCommand = "gcloud services list --project " + str(output[i]) + " --format=table(TITLE)"
        print(bashCommand)
        process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
        output2, error = process.communicate()
        # convert from binary to plaintext string if necessary
        if type(output2) == type(b''): output2 = output2.decode('ascii')
        # remove the first line of the output which is just 'TITLE\n' (6 characters)
        output2 = output2[6:]   

        '''
        # uncomment this code if you want the output to be split into 2 columns for formatting reasons
        # if you do uncomment this section, make sure to comment out the writer.writerow([output[i], output2]) on line 68

        # count the number of newlines and find the row which would be considered the middle
        midpoint = output2.count('\n') // 2
        for j in range(len(output2)):
            if output2[j] == '\n':
                midpoint -= 1
                if midpoint == 0: break
        str1 = output2[:j]
        str2 = output2[j+1:]
        writer.writerow([output[i], str1, str2])
        '''

        # write the outputs to the file specified by OUTPUT_FILE_NAME
        writer.writerow([output[i], output2])
