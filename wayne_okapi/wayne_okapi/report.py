from jinja2 import Template
import time


def generateReport(data) :
    html_template = '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>接口测试报告</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@3.3.7/dist/js/bootstrap.min.js" integrity="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa" crossorigin="anonymous"></script>
        <script src="http://cdn.highcharts.com.cn/highcharts/highcharts.js"></script>
    </head>
    <body>
        <div class="container-fluid">

            <nav class="navbar navbar-inverse navbar-static-top">
                <div class="container-fluid">
                    <div class="navbar-header">
                        <a class="navbar-brand" style="font-weight: bold;color: whitesmoke" href="https://github.com/zachlau">
                            OK-API
                        </a>
                    </div>
                </div>
            </nav>

            <div class="row">
                <div class="col-md-4 col-sm-4 col-xs-4">
                    <h4>REPORT {{times}}</h4>
                    <footer>{{data['start_time']}} - {{data['end_time']}}</footer>
                    <h2 style="text-align: center;margin-top: 50px"><button style="width: 150px" class="btn btn-primary btn-lg">{{data['total']}}</button></h2>
                    <p style="text-align: center">用例总数</p>
                </div>
                <div class="col-md-4 col-sm-4 col-xs-4">
                    <div id="chart" style="width: 500px;height:350px;"></div>
                </div>
            </div>

            <div class="row">
                <div class="col-md-6 col-sm-6 col-xs-6" style="margin-top: -80px">
                    <h4>ENVIRONMENT</h4>
                    <table class="table table-bordered table-striped" style="margin-top: 20px;font-size: 16px">
                        <tr>
                            <th>变量名</th>
                            <th>变量值</th>
                        </tr>
                        <tbody>
                            {% for k,v in data['environment'].items() %}
                            <tr>
                                <td>{{k|e}}</td>
                                <td>{{v|e}}</td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            </div>

            <hr class="simple" color="	#F0F8FF" style="height: 2px"/>

            <div class="row" style="margin-top: 20px">
                <div class="col-md-10 col-sm-10 col-xs-10">
                    <h4>CASES</h4>
                      <!-- Nav tabs -->
                    <ul class="nav nav-tabs" role="tablist">
                        <li role="presentation" class="active"><a style="font-weight: bold" href="#all" class="btn btn-info" aria-controls="home" role="button" data-toggle="tab">汇总（{{data['total']}}）</a></li>
                        <li role="presentation"><a class="btn btn-success" href="#success" aria-controls="profile" role="button" data-toggle="tab">成功（{{data['success']}}）</a></li>
                        <li role="presentation"><a href="#danger" class="btn btn-danger" aria-controls="messages" role="button" data-toggle="tab">失败（{{data['failed']}}）</a></li>
                        <li role="presentation"><a href="#warning" class="btn btn-warning" aria-controls="settings" role="button" data-toggle="tab">跳过（{{data['skip']}}）</a></li>
                    </ul>

                    <div class="tab-content">

                        <div role="tabpanel" class="tab-pane active" id="all">
                            <table class="table table-bordered table-striped" style="margin-top: 20px;font-size: 16px">
                                <tr>
                                    <th>用例编号</th>
                                    <th>用例名称</th>
                                    <th>日志信息</th>
                                </tr>
                                <tbody>
                                {% for case in data['cases'] %}
                                    {% if case['status'] == 0 %}
                                        <tr class="text-success">
                                    {% elif case['status'] == 1 %}
                                        <tr class="text-danger">
                                    {% elif case['status'] == 2 %}
                                        <tr class="text-warning">
                                    {% endif %}
                                        <td>{{case['id']}}</td>
                                        <td>{{case['name']}}</td>
                                        <td>{{case['log']}}</td>
                                    </tr>
                                {% endfor %}
                                </tbody>
                            </table>
                        </div>

                        <div role="tabpanel" class="tab-pane" id="success">
                            <table class="table table-bordered table-striped" style="margin-top: 20px;font-size: 16px">
                                <tr>
                                    <th>用例编号</th>
                                    <th>用例名称</th>
                                    <th>日志信息</th>
                                </tr>
                                <tbody class="text-success">
                                    {% for case in data['cases'] %}
                                        {% if case['status'] == 0 %}
                                            <tr>
                                                <td>{{case['id']}}</td>
                                                <td>{{case['name']}}</td>
                                                <td>{{case['log']}}</td>
                                            </tr>
                                        {% endif %}
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>

                        <div role="tabpanel" class="tab-pane" id="danger">
                            <table class="table table-bordered table-striped" style="margin-top: 20px;font-size: 16px">
                                <tr>
                                    <th>用例编号</th>
                                    <th>用例名称</th>
                                    <th>日志信息</th>
                                </tr>
                                <tbody class="text-danger">
                                    {% for case in data['cases'] %}
                                        {% if case['status'] == 1 %}
                                            <tr>
                                                <td>{{case['id']}}</td>
                                                <td>{{case['name']}}</td>
                                                <td>{{case['log']}}</td>
                                                <td>{{case['res']}}</td>
                                            </tr>
                                        {% endif %}
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>

                        <div role="tabpanel" class="tab-pane" id="warning">
                            <table class="table table-bordered table-striped" style="margin-top: 20px;font-size: 16px">
                                <tr>
                                    <th>用例编号</th>
                                    <th>用例名称</th>
                                    <th>日志信息</th>
                                </tr>
                                <tbody class="text-warning">
                                   {% for case in data['cases'] %}
                                        {% if case['status'] == 2 %}
                                            <tr>
                                                <td>{{case['id']}}</td>
                                                <td>{{case['name']}}</td>
                                                <td>{{case['log']}}</td>
                                            </tr>
                                        {% endif %}
                                    {% endfor %}
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>

        </div>

        <script>
            Highcharts.setOptions({
                colors: ['#50B432', '#ED561B', '#FFF263']
            });
            var chart = Highcharts.chart('chart', {
                credits: {
                    enabled:false
                },
                title: {
                    text: '测试用例',
                    align: 'center',
                    verticalAlign: 'middle',
                    y: 80
                },
                tooltip: {
                    headerFormat: '{series.name}<br>',
                    pointFormat: '{point.name}: <b>{point.percentage:.1f}%</b>'
                },
                plotOptions: {
                    pie: {
                        dataLabels: {
                            enabled: true,
                            distance: -50,
                            style: {
                                fontWeight: 'bold',
                                color: 'white',
                                fontSize: '14px',
                                textShadow: '0px 1px 2px black'
                            }
                        },
                        startAngle: -90, // 圆环的开始角度
                        endAngle: 90,    // 圆环的结束角度
                        center: ['50%', '75%']
                    }
                },
                series: [{
                    type: 'pie',
                    name: '测试用例',
                    innerSize: '50%',
                    data: [
                        ['成功',   {{data['success']}}],
                        ['失败', {{data['failed']}}],
                        ['跳过',   {{data['skip']}}],
                    ],
                    dataLabels: {
			            enabled: false
		            }
                }]
            });
        </script>
    </body>
    </html>'''

    template = Template(html_template)
    now = time.time()
    tmp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(now))
    content = template.render(times=tmp, data=data)
    tmp2 = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(now))
    with open('./reports/{tmp}.html'.format(tmp=tmp2), 'wb') as f :
        f.write(content.encode(encoding='utf-8'))


data = {"total" : 100, "success" : 75, "failed" : 22, "skip" : 1,
        "environment" : {"根路径" : "http://118.24.91.97:9000/api/",
                         "启用全局Session" : "TRUE"},
        "start_time" : "11:15:05",
        "end_time" : "12:28:04",
        "cases" : [
            {"id" : "login01", "name" : "正确登录", "status" : 0, "log" : "响应状态码验证成功！\n响应Json值验证成功！"},
            {"id" : "get_city01", "name" : "获取城市信息", "status" : 1, "log" : "响应状态码验证失败！\n响应Json值验证失败！", "res" : "xxxx"},
            {"id" : "get_city02", "name" : "	城市信息错误", "status" : 2, "log" : "请求体参数配置错误！"}
        ]
        }
# generateReport(data=data)

{'cases': [{'id': 'get_city01', 'name': '获取城市信息', 'status': 2, 'log': '请求体格式无效'}], 'total': 3, 'environment': ({'根路径': 'http://118.24.91.97:9000/api/', '启用全局Session': 'TRUE'},), 'start_time': '23:48:07'}
