<%@ page language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="description" content="">
<meta name="keywords" content="">
<meta name="viewport"
	content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">

<!-- Set render engine for 360 browser -->
<meta name="renderer" content="webkit">

<!-- No Baidu Siteapp -->
<meta http-equiv="Cache-Control" content="no-siteapp" />
<link rel="icon" type="image/png" href="assets/i/favicon.png">
<!-- <link rel="icon" type="image/png" href="assets/i/banner1.png"> -->

<!-- Add to homescreen for Chrom on Android -->
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black">
<meta name="apple-mobile-web-app-title" content="Amaze UI" />
<link rel="apple-touch-icon-precomposed"
	href="assets/i/app-icon72x72@2x.png">

<!-- Tile icon for Win8 (144x144 + tile color) -->
<meta name="msapplication-TileImage"
	content="assets/i/app-icon72x72@2x.png">
<meta name="msapplication-TileColor" content="#0e90d2">


<link rel="stylesheet" href="assets/css/amazeui.css">
<link rel="stylesheet" href="assets/css/admin.css">
<link rel="stylesheet" href="assets/css/app.css">
<script src="assets/js/jquery.min.js"></script>
<script src="assets/js/amazeui.min.js"></script>
<script src="assets/js/getParameter.js"></script>
<title>Welcome PMT4I!</title>

<script type="text/javascript">
			/*$(document).ready(function(){
				$('testButton').click(function(){
					form();
				});
			});*/
			var excel_Route;
			//初始化
			function start(){
				document.getElementById("showimagelength").innerHTML = getParameter("imagelength");
				var MR=getParameter("MR");
				var param=getParameter("param");
				if(MR=="0"){
					document.getElementById('table1').innerHTML="1：改变对比度";
				}else if(MR=="1"){
					document.getElementById('table1').innerHTML="2：改变亮度";
				}else if(MR=="2"){
					document.getElementById('table1').innerHTML="3：噪声处理";
				}else if(MR=="3"){
					document.getElementById('table1').innerHTML="4：仿射变换";
				}else if(MR=="4"){
					document.getElementById('table1').innerHTML="5：微小平移";
				}else if(MR=="5"){
					document.getElementById('table1').innerHTML="6：微小旋转";
				}else if(MR=="6"){
					document.getElementById('table1').innerHTML="7：微小放大";
				}else if(MR=="7"){
					document.getElementById('table1').innerHTML="8：微小缩小";
				}else if(MR=="8"){
					document.getElementById('table1').innerHTML="9：模糊处理+微小旋转";
				}else if(MR=="9"){
					document.getElementById('table1').innerHTML="10：改变锐度+微小旋转";
				}else if(MR=="10"){
					document.getElementById('table1').innerHTML="11：微小侵蚀+微小旋转";
				}else if(MR=="11"){
					document.getElementById('table1').innerHTML="12：微小膨胀+微小旋转";
				}
				if(MR=="0"){
					if(param=="1"){
						document.getElementById('table2').innerHTML="95%";
					}else if(param=="2"){
						document.getElementById('table2').innerHTML="90%";
					}else if(param=="3"){
						document.getElementById('table2').innerHTML="85%";
					}else if(param=="4"){
						document.getElementById('table2').innerHTML="80%";
					}else if(param=="5"){
						document.getElementById('table2').innerHTML="75%";
					}
				}else if(MR=="1"){
					if(param=="1"){
						document.getElementById('table2').innerHTML="5";
					}else if(param=="2"){
						document.getElementById('table2').innerHTML="10";
					}else if(param=="3"){
						document.getElementById('table2').innerHTML="15";
					}else if(param=="4"){
						document.getElementById('table2').innerHTML="20";
					}else if(param=="5"){
						document.getElementById('table2').innerHTML="25";
					}
				}else if(MR=="2"){
					document.getElementById('table2').innerHTML="无";
				}else if(MR=="3" || MR=="4" || MR=="6" || MR=="7"){
					if(param=="1"){
						document.getElementById('table2').innerHTML="0.01";
					}else if(param=="2"){
						document.getElementById('table2').innerHTML="0.02";
					}else if(param=="3"){
						document.getElementById('table2').innerHTML="0.03";
					}else if(param=="4"){
						document.getElementById('table2').innerHTML="0.04";
					}else if(param=="5"){
						document.getElementById('table2').innerHTML="0.05";
					}
				}else if(MR=="5" || MR=="8" || MR=="9" || MR=="10" || MR=="11"){
					if(param=="1"){
						document.getElementById('table2').innerHTML="1.6°";
					}else if(param=="2"){
						document.getElementById('table2').innerHTML="1.8°";
					}else if(param=="3"){
						document.getElementById('table2').innerHTML="2.0°";
					}else if(param=="4"){
						document.getElementById('table2').innerHTML="2.2°";
					}else if(param=="5"){
						document.getElementById('table2').innerHTML="2.4°";
					}
				}
				document.getElementById('table3').innerHTML=getParameter("folder");
				document.getElementById('table4').innerHTML=getParameter("sortType");
				document.getElementById('table5').innerHTML=getParameter("filename");
			}
			
			//执行测试
			function doform(){
				//获得参数
				var imageRows = $("#imageRows").val();//没填为""
				//信息填写完整后执行测试
				if(imageRows==""){
					alert("请将信息填写完整！");
				}else{
					//获得参数
					var MR=getParameter("MR");
					var param=getParameter("param");
					var probabilisticType=$('input[type=radio][name=radio]').filter(":checked").attr("value");
					var readExcelRoute=getParameter("readExcelRoute");
					var sortType=getParameter("sortType");
					
					//输入参数
					var formdata = new FormData();
					formdata.append("MR",MR);
					formdata.append("param",param);
					formdata.append("probabilisticType",probabilisticType);
					formdata.append("readExcelRoute",readExcelRoute);
					formdata.append("sortType",sortType);
					formdata.append("imageRows",imageRows);
					
					//设置进度条
					document.getElementById("progress-show").style.display="";
					
					//ajax调用后端
					$.ajax({
						type:"post",
						url:"testMain",
						data:formdata,
						processData:false,
						contentType:false,
						success:function(excelResult){
							//显示测试结果
							excel_Route=excelResult.excelRoute;
							var all_Num=excelResult.allNum;
							var error_Num=excelResult.errorNum;
							var error_Ratio=new Number(error_Num/all_Num*100);
							document.getElementById('table6').innerHTML=all_Num;
							document.getElementById('table7').innerHTML=error_Num;
							document.getElementById('table8').innerHTML=error_Ratio.toFixed(2)+"%";
							//取消进度条
							document.getElementById("progress-show").style.display="none";
							document.getElementById("table_result").style.display="";
							document.getElementById("button_download_show").style.visibility = "visible";
							document.getElementById("button_next").style.visibility = "visible";
						},
						error:function(e){
							alert("失败了"+e.status);
							//取消进度条
							document.getElementById("progress-show").style.display="none";
							document.getElementById("table_result").style.display="none";
							document.getElementById("button_download_show").style.visibility = "hidden";
							document.getElementById("button_next").style.visibility = "hidden";
						}
					});
				}
			}
			function download(){
				javascript:location.href='fileDownload?excelRoute='+excel_Route;
			}
			function next(){
				var folder=getParameter("folder");
				window.open('showResult.jsp?folder='+folder+'&excelRoute='+excel_Route);
			}
		</script>

</head>

<body onload="start()">
	<!-- 编写代码 -->
	<!-- 标题 -->
	<header class="am-topbar am-topbar-inverse admin-header">
		<div class="am-topbar-brand">
			<!-- <strong><font size="5">Supporting Tool of Metamorphic Testing for Image Processing Software</font></strong> <small><font size="5">MT4I</font></small> -->
			<strong>Supporting Tool of Probabilistic Metamorphic Testing
				for Image Classification Software</strong> <small>PMT4I</small>
		</div>
	</header>
	<!-- 主内容 -->
	<div class="am-cf admin-main">
		<!-- 左侧边栏 -->
		<div class="admin-sidebar am-offcanvas" id="admin-offcanvas">
			<div class="am-offcanvas-bar admin-offcanvas-bar">
				<ul class="am-list admin-siderbar-list">
					<li><a href="index.jsp" style="color: #006699;"><span
							class="am-icon-sign-out"></span> 开始</a></li>
					<li><a style="color: #000000;"><span
							class="am-icon-sign-out"></span> 选择蜕变关系</a></li>
					<!--selectMRs.jsp -->
					<li><a style="color: #000000;"><span
							class="am-icon-sign-out"></span> 上传待测对象</a></li>
					<!--getProgram.jsp -->
					<li><a style="color: #000000; background-color: #B0C4DE;"><span
							class="am-icon-sign-out"></span> 执行测试</a></li>
					<!--PMT.jsp -->
					<li><a style="color: #000000;"><span
							class="am-icon-sign-out"></span> 查看测试结果</a></li>
					<!--showResult.jsp -->
				</ul>
				<div class="am-panel am-panel-default admin-siderbar-panel">
					<div class="am-panel-bd">
						<p>
							<!-- <img src="assets/i/banner1.png" width="40">-->
							<span class="am-icon-tag"></span>
							<!-- <font size="5">欢迎</font> -->
							欢迎
							<!-- Welcome -->
						</p>
						<p>
							<!-- <font size="5">欢迎使用MT4I！</font> -->
							欢迎使用PMT4I！
							<!-- Welcome to MT4I! -->
						</p>
					</div>
				</div>
			</div>
		</div>

		<!-- 右侧主内容 -->
		<div class="admin-content">
			<div class="admin-content-body">
				<!-- 右侧小标题 -->
				<div class="am-cf am-padding am-padding-bottom-0">
					<div class="am-fl am-cf">
						<strong class="am-text-primary am-text-lg"> <!-- <font size="5">执行蜕变测试</font> -->执行测试
						</strong>
					</div>
				</div>
				<hr>

				<!-- 右侧主内容 -->
				<div class="am-g">
					<!-- 使用说明 -->
					<!-- 工具主要内容 -->
					<div class="am-u-lg-12">
						<div class="am-panel am-panel-default">
							<div class="am-panel-hd am-cf"
								data-am-collapse="{target: '#collapse-panel-3'}">
								<strong>使用说明</strong> <span class="am-icon-chevron-down am-fr"></span>
							</div>
							<div class="am-panel-bd am-cf am-collapse am-in"
								id="collapse-panel-3">
								<div class="am-panel am-panel-default admin-sidebar-panel">
									<div class="am-panel-bd">
										<p>（1）填写需要使用的原始图像数量；</p>
										<p>（2）选择测试方法；</p>
										<p>（3）点击“开始测试”执行测试方法，测试结束后页面会展示测试图像总数量、未通过测试的图像数量和未通过测试比率，同时页面显示出“下载测试日志”和“查看测试结果”按钮；</p>
										<p>（4）点击“下载测试日志”获得包含测试结果的excel文件；</p>
										<p>（5）点击“查看测试结果”进入“查看测试结果”步骤。</p>
									</div>
								</div>
							</div>
						</div>
						<div class="am-panel am-panel-default">
							<div class="am-panel-hd am-cf"
								data-am-collapse="{target: '#collapse-panel-1'}">
								<strong>参数详情</strong> <span class="am-icon-chevron-down am-fr"></span>
							</div>
							<div class="am-panel-bd am-cf am-collapse am-in"
								id="collapse-panel-1">
								<table
									class="am-table am-table-striped am-table-hover am-table-bordered am-table-radius"
									style="margin-top: 20px">
									<!-- 
										<tr>
											<th style="width:20%;text-align: center;">蜕变关系</th>
											<td style="text-align: center;"><span id="table1" >0</span></td>
										</tr>
										<tr>
											<th style="text-align: center;">蜕变关系参数</th>
											<td style="text-align: center;"><span id="table2" >0</span></td>
										</tr>
										<tr>
											<th style="text-align: center;">原始图像文件夹</th>
											<td style="text-align: center;"><span id="table3" >0</span></td>
										</tr>
										<tr>
											<th style="text-align: center;">原始图像排序方式</th>
											<td style="text-align: center;"><span id="table4" >0</span></td>
										</tr>
										<tr>
											<th style="text-align: center;">待测文件</th>
											<td style="text-align: center;"><span id="table5" >0</span></td>
										</tr>
										-->
									<thead>
										<tr>
											<th style="text-align: center;">蜕变关系</th>
											<th style="text-align: center;">蜕变关系参数</th>
											<th style="text-align: center;">原始图像文件夹</th>
											<th style="text-align: center;">原始图像排序方式</th>
											<th style="text-align: center;">待测文件</th>
										</tr>
									</thead>
									<tbody>
										<tr>
											<td style="text-align: center;"><span id="table1">0</span></td>
											<td style="text-align: center;"><span id="table2">0</span></td>
											<td style="text-align: center;"><span id="table3">0</span></td>
											<td style="text-align: center;"><span id="table4">0</span></td>
											<td style="text-align: center;"><span id="table5">0</span></td>
										</tr>
									</tbody>
								</table>
							</div>
						</div>
						<!-- 选择原始图像数量与测试方法 -->
						<div class="am-panel am-panel-default">
							<div class="am-panel-hd">
								<h4 class="am-panel-title">
									<strong> <!-- <font size="5">选择蜕变关系与具体参数</font> -->选择原始图像数量与测试方法
									</strong>
								</h4>
							</div>
							<div class="am-panel-bd">
								<div class="am-g" align="center" id="type_two_number">
									<hr>
									<input type="text" id="imageRows" name="imageRows" value=""
										placeholder="输入原始图像数量（如：10）" style="text-align: center">
									/
									<div align="center" id="showimagelength"
										style="display: inline-block;">1000</div>
									张原始图像
								</div>
								<hr>
								<div class="am-g" align="center">
									<div id="radiogroup" class="am-form-group">
										<label class="am-radio-inline" id="hiddenradio1"> <input
											id="radio1" type="radio" name="radio" value="MT"
											data-am-ucheck checked> <!-- <div id="radioone" style="font-size:25px">BRG</div> -->
											<div id="radioone">MT</div>
										</label> <label class="am-radio-inline" id="hiddenradio2"> <input
											id="radio2" type="radio" name="radio" value="Jaccard"
											data-am-ucheck> <!-- <div id="radiotwo" style="font-size:25px">RGB</div> -->
											<div id="radiotwo">PMT-Jaccard</div>
										</label> <label class="am-radio-inline" id="hiddenradio3"> <input
											id="radio3" type="radio" name="radio" value="Wilcoxon"
											data-am-ucheck> <!-- <div id="radiothree" style="font-size:25px">RBG</div> -->
											<div id="radiothree">PMT-Wilcoxon</div>
										</label>
									</div>
								</div>
								<hr>

								<!-- 执行按钮 -->
								<div class="am-g" align="center">
									<button type="button"
										class="am-btn am-btn-primary am-btn-default am-btn-block"
										id="testButton" onclick="doform()" style="width: 50%">
										<!-- <font size="5">开始测试</font> -->
										开始测试
									</button>
								</div>
							</div>
						</div>
						<!-- 执行进度条 -->
						<div id="progress-show"
							class="am-progress am-progress-striped am-active"
							style="display: none">
							<div id="progress" class="am-progress-bar" style="width: 100%"></div>
						</div>
						<!-- 测试结果显示表格 -->
						<table id="table_result"
							class="am-table am-table-striped am-table-hover am-table-bordered am-table-radius"
							style="margin-top: 20px; display: none;">
							<thead>
								<tr>
									<th style="text-align: center;">测试图像总数量</th>
									<th style="text-align: center;">未通过测试的图像数量</th>
									<th style="text-align: center;">未通过测试比率</th>
								</tr>
							</thead>
							<tbody>
								<tr>
									<td style="text-align: center;"><span id="table6">0</span></td>
									<td style="text-align: center;"><span id="table7">0</span></td>
									<td style="text-align: center;"><span id="table8">0</span></td>
								</tr>
							</tbody>
						</table>
						<!-- 下载日志 -->
						<div class="am-g">
							<div id="button_download_show" class="am-u-lg-6" align="center"
								style="visibility: hidden">
								<button type="button" class="am-btn am-btn-primary am-btn-block"
									name="button_download" id="button_download"
									onclick="download()" style="width: 50%">
									<!-- <font size="5">下载测试日志</font> -->
									下载测试日志
								</button>
							</div>
							<div id="button_next" class="am-u-lg-6" align="center"
								style="visibility: hidden">
								<button type="button" class="am-btn am-btn-primary am-btn-block"
									name="button_PMT" id="button_PMT" onclick="next()"
									style="width: 50%">
									<!-- <font size="5">下载测试日志</font> -->
									查看测试结果
								</button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>


	<a href="#"
		class="am-icon-btn am-icon-th-list am-show-sm-only admin-menu"
		data-am-offcanvas="{target: '#admin-offcanvas'}"></a>
</body>
</html>