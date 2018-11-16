from data import CaseData,OtherData,ProjectData
from os import path
from re import sub
import csv


casesObject = CaseData()
cases = casesObject.cases
csvFileDir = path.join(path.dirname(path.realpath(__file__)),"..","experiment-runner","inputs","inputs.csv")
csvFile = open(csvFileDir,"wb")
writer = csv.writer(csvFile)
fieldnames = ['execution_idx', 'application', 'case', 'version', 'classpath', 'package',
              'stacktrace_path', 'fixed', 'fixed_version', 'buggy_frame',
              'p_functional_mocking', 'functional_mocking_percent',
              'p_reflection_on_private','reflection_start_percent',
              'search_budget','population','p_object_pool','p_model_pool_target_init', 'p_model_pool_non_target_init','seed_clone','seed_mutations', 'test_dir']
writer.writerow(fieldnames)

for index,case in enumerate(cases):

    project = ProjectData().findProject(case["project"])
    for i in range(0,OtherData().repeat):
        for prob in OtherData().p_functional_mocking:
            for percent in OtherData().functional_mocking_percent:
                for time in OtherData().search_budget:
                    for pop in OtherData().population:
                        for sc in OtherData().seed_clone:
                            for sm in OtherData().seed_mutations:
                                for pobj in OtherData().p_object_pool:
                                    for pmodel in OtherData.p_model_pool_init:
                                        classpath = path.join("becnhmark","applications",project["name"].upper()+"-bins",project["name"].upper()+"-"+case["version"])
                                        stacktracePath = path.join("becnhmark","crashes",project["name"].upper(),case["name"],case["name"]+".log")
                                        testDir = path.join("JarFiles","GGA-tests",case["name"])
                                        row = []
                                        row.append(i+1)
                                        row.append(project["name"])
                                        row.append(case["name"])
                                        row.append(case["version"])
                                        row.append(classpath)
                                        row.append(project["package"])
                                        row.append(stacktracePath)
                                        row.append("yes" if case["fixed"]=="1" else "no")
                                        row.append(case["fixed_version"])
                                        row.append(sub("[^0-9]", "",case["buggy_frame"]))
                                        row.append(prob)
                                        row.append(percent)
                                        row.append(0)
                                        row.append(0)
                                        row.append(time)
                                        row.append(pop)
                                        row.append(pobj)
                                        row.append(pmodel[0])
                                        row.append(pmodel[1])
                                        row.append(sc)
                                        row.append(sm)
                                        row.append(testDir)
                                        writer.writerow(row)


csvFile.close()

