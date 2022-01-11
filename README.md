# get-services
Script to get the services for a GCP organization using gcloud and bash commands.

Can be run with 'python get-services.py'.

You can change the name of the output file by changing the OUTPUT_FILE_NAME variable in the code.

Make sure you're logged into gcloud before running by using 'gcloud auth login'. If not, you can uncomment the section that does it for you however it requires some user input.

Can be fitted to find other project information such as labels, log-sinks, and pretty much any other info under a project assuming you have the correct permissions. Simply change <b><i>bashCommand = "gcloud services list --project " + str(output[i]) + " --format=table(TITLE)"</b></i> to whatever gcloud command would produce the desired output.
