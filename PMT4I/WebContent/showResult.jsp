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
			//初始化
			function start(){
				//获得参数
				var folder=getParameter("folder");
				var excelRoute=getParameter("excelRoute");
				//输入参数
				var formdata = new FormData();
				formdata.append("excelRoute",excelRoute);
				//ajax调用后端
				$.ajax({
					type:"post",
					url:"getResult",
					data:formdata,
					processData:false,
					contentType:false,
					success:function(result){
						//显示测试结果
						document.getElementById('table1').innerHTML=result.time;
						var MR=result.mr-1;
						var param=result.param;
						if(MR=="0"){
							document.getElementById('table2').innerHTML="1：改变对比度";
						}else if(MR=="1"){
							document.getElementById('table2').innerHTML="2：改变亮度";
						}else if(MR=="2"){
							document.getElementById('table2').innerHTML="3：噪声处理";
						}else if(MR=="3"){
							document.getElementById('table2').innerHTML="4：仿射变换";
						}else if(MR=="4"){
							document.getElementById('table2').innerHTML="5：微小平移";
						}else if(MR=="5"){
							document.getElementById('table2').innerHTML="6：微小旋转";
						}else if(MR=="6"){
							document.getElementById('table2').innerHTML="7：微小放大";
						}else if(MR=="7"){
							document.getElementById('table2').innerHTML="8：微小缩小";
						}else if(MR=="8"){
							document.getElementById('table2').innerHTML="9：模糊处理+微小旋转";
						}else if(MR=="9"){
							document.getElementById('table2').innerHTML="10：改变锐度+微小旋转";
						}else if(MR=="10"){
							document.getElementById('table2').innerHTML="11：微小侵蚀+微小旋转";
						}else if(MR=="11"){
							document.getElementById('table2').innerHTML="12：微小膨胀+微小旋转";
						}
						if(MR=="0"){
							if(param=="1"){
								document.getElementById('table3').innerHTML="95%";
							}else if(param=="2"){
								document.getElementById('table3').innerHTML="90%";
							}else if(param=="3"){
								document.getElementById('table3').innerHTML="85%";
							}else if(param=="4"){
								document.getElementById('table3').innerHTML="80%";
							}else if(param=="5"){
								document.getElementById('table3').innerHTML="75%";
							}
						}else if(MR=="1"){
							if(param=="1"){
								document.getElementById('table3').innerHTML="5";
							}else if(param=="2"){
								document.getElementById('table3').innerHTML="10";
							}else if(param=="3"){
								document.getElementById('table3').innerHTML="15";
							}else if(param=="4"){
								document.getElementById('table3').innerHTML="20";
							}else if(param=="5"){
								document.getElementById('table3').innerHTML="25";
							}
						}else if(MR=="2"){
							document.getElementById('table3').innerHTML="无";
						}else if(MR=="3" || MR=="4" || MR=="6" || MR=="7"){
							if(param=="1"){
								document.getElementById('table3').innerHTML="0.01";
							}else if(param=="2"){
								document.getElementById('table3').innerHTML="0.02";
							}else if(param=="3"){
								document.getElementById('table3').innerHTML="0.03";
							}else if(param=="4"){
								document.getElementById('table3').innerHTML="0.04";
							}else if(param=="5"){
								document.getElementById('table3').innerHTML="0.05";
							}
						}else if(MR=="5" || MR=="8" || MR=="9" || MR=="10" || MR=="11"){
							if(param=="1"){
								document.getElementById('table3').innerHTML="1.6°";
							}else if(param=="2"){
								document.getElementById('table3').innerHTML="1.8°";
							}else if(param=="3"){
								document.getElementById('table3').innerHTML="2.0°";
							}else if(param=="4"){
								document.getElementById('table3').innerHTML="2.2°";
							}else if(param=="5"){
								document.getElementById('table3').innerHTML="2.4°";
							}
						}
						document.getElementById('table4').innerHTML=folder;
						document.getElementById('table5').innerHTML=result.sortType;
						document.getElementById('table6').innerHTML=result.fileName;
						document.getElementById('table7').innerHTML=result.probabilisticType;
						var all_Num=result.allNum;
						var error_Num=result.errorNum;
						var error_Ratio=new Number(error_Num/all_Num*100);
						document.getElementById('table8').innerHTML=all_Num;
						document.getElementById('table9').innerHTML=error_Num;
						document.getElementById('table10').innerHTML=error_Ratio.toFixed(2)+"%";
						document.getElementById("table_result").style.display="";
						//图像测试详情
						var image_result_lis=
							'<table class="am-table am-table-striped am-table-hover am-table-bordered am-table-radius" style="margin-top:20px;">\n'+
							'	<thead>\n'+
							'  		<tr>\n'+
							'   		<th style="text-align: center;">序号</th>\n'+
							'    		<th style="text-align: center;">测试图像</th>\n'+
							'    		<th style="text-align: center;">测试结果</th>\n'+
							'  		</tr>\n'+
							'	</thead>\n'+
							'	<tbody>\n';
						var image_results=result.imageResults;
						for(var i=0;i<image_results.length;i++){
							var image_result = image_results[i];
							var showType="测试通过";
							if(image_result.resultType==0){
								showType="测试未通过";
							}
							var li = 
								'		<tr>\n'+
								'  			<td style="text-align: center;"><span>'+(i+1)+'</span></td>\n'+
								'  			<td style="text-align: center;"><span>'+image_result.path+'</span></td>\n'+
								'  			<td style="text-align: center;"><span>'+showType+'</span></td>\n'+
								'		</tr>\n';
							image_result_lis +=li;
						}
						image_result_lis += '	</tbody>\n</table>';
						$('#addImageResult').html(image_result_lis);
						//定位到页面顶部
						//window.scrollTo(0,0);
					},
					error:function(e){
						alert("失败了"+e.status);
					}
				});
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
					<li><a style="color: #000000;"><span
							class="am-icon-sign-out"></span> 执行测试</a></li>
					<!--PMT.jsp -->
					<li><a style="color: #000000; background-color: #B0C4DE;"><span
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
						<strong class="am-text-primary am-text-lg"> <!-- <font size="5">执行蜕变测试</font> -->查看测试结果
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
										<p>（1）页面展示详细测试结果。</p>
									</div>
								</div>
							</div>
						</div>
						<div class="am-panel am-panel-default">
							<div class="am-panel-hd">
								<h4 class="am-panel-title">
									<strong>测试详情</strong>
								</h4>
							</div>
							<div class="am-panel-bd">
								<table id="table_result"
									class="am-table am-table-striped am-table-hover am-table-bordered am-table-radius"
									style="margin-top: 20px; display: none;">
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
											<th style="text-align: center;">日期</th>
											<th style="text-align: center;">蜕变关系</th>
											<th style="text-align: center;">蜕变关系参数</th>
											<th style="text-align: center;">原始图像文件夹</th>
											<th style="text-align: center;">原始图像排序方式</th>
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
									<thead>
										<tr>
											<th style="text-align: center;">待测文件</th>
											<th style="text-align: center;">测试方法</th>
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
											<td style="text-align: center;"><span id="table9">0</span></td>
											<td style="text-align: center;"><span id="table10">0</span></td>
										</tr>
									</tbody>
								</table>
							</div>
						</div>
						<div class="am-panel am-panel-default">
							<div class="am-panel-hd">
								<h4 class="am-panel-title">
									<strong>图像测试详情</strong>
								</h4>
							</div>
							<div class="am-panel-bd">
								<div class="am-g">
									<!-- 测试结果显示表格 -->
									<ul id="addImageResult"></ul>
								</div>
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