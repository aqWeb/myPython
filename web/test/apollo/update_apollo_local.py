from web.test.common.file.aleter_file import alter

application = [
    'xxl.job.executor.appname=aaaa'
]

jcxlf_system = [
    'eureka.client.service-url.defaultZone=http://localhost:8761/eureka/',
    'server.port=8080'
]

default_000 = [

]

model = 'credit'
base_path = "C:/opt/data/loan2.1-jcxlf-%s/config-cache" % model
default_application_properties = "%s/loan2.1-jcxlf-%s+default+application.properties" % (base_path, model)
default_jcxlf_system_properties = "%s/loan2.1-jcxlf-%s+default+jcxlf.system.properties" % (base_path, model)
default_000_properties = "%s/loan2.1-jcxlf-%s+default+000.properties" % (base_path, model)


def do_update(param, path):
    for line in param:
        if "=" in line:
            key = line.split("=")[0]
            xxx = line + "\n"
            alter(path, key, xxx)
        else:
            print("没有=分隔符")
            continue


def do_update_job():
    job = "C:\opt\data\loan2.1-jcxlf-job-admin\config-cache\loan2.1-jcxlf-job-admin+default+application.properties"
    job_admin_application = [
        'server.port=9090'
    ]
    do_update(job_admin_application, job)
    # dev
    f1 = 'C:/opt/settings/server.properties'
    old = '#env=local'
    new = 'env=local\n'
    alter(f1, old, new)
    old = 'env=DEV'
    new = '#env=DEV'
    alter(f1, old, new)


# do_update(application, default_application_properties)
do_update(jcxlf_system, default_jcxlf_system_properties)
do_update(default_000, default_000_properties)
do_update_job()
print("修改配置完成")
