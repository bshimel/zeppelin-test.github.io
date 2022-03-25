import os
import os.path
import filecmp
import shutil

content_path = '/Users/bshimel/dev/contentFactory'
ztest_path = '/Users/bshimel/dev/ztest'

manifest = open(content_path + "/courses/DataEngineeringTraining.manifest", 'r');

lines = manifest.readlines()

print("Checking manifest...",end='')
for line in lines:
    type, file = line.split('|')
    file = file.strip()
    if type.startswith('Lab') or type.startswith('Demo'):
        if not(os.path.exists(content_path + "/notebooks/" + file)):
            print("Missing from contentFactory: " + file)
        if not(file.startswith('DE')):
            print("Does not start with DE: " + file)
        if not(os.path.exists(ztest_path + "/notebooks/" + file)):
            print("Missing from ztest: " + file)
            shutil.copy2(content_path + "/notebooks/" + file, ztest_path + "/notebooks/" + file)
        elif not(filecmp.cmp(content_path + "/notebooks/" + file, ztest_path + "/notebooks/" + file)):
            print("contentFactory and ztest do not match: " + file)
print("Done.")
