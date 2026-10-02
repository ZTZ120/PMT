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
			var excelRoute;
			var nextFileName;
			//选择待测文件
			function getFileButton(){
				//触发file选择
				document.getElementById('getfile').click();
			}
			//file选择文件
			function getFile(){
				//显示待测文件名
				var file = document.getElementById('getfile').files[0];
				document.getElementById("filepath").innerHTML = file.name;
				
			}
			//原始图片文件夹选择
			function getImageFolderButton(){
				//file选择文件夹
				document.getElementById('imagefolder').click();
				
			}
			//触发file选择文件夹
			function getImageFolder(){
				/*var folderpath = document.getElementById('imagefolder').value;
				var folder = folderpath.substring(0,folderpath.lastIndexOf('\\'));
				document.getElementById('folder').innerHTML = folder;*/
				var file = document.getElementById('imagefolder').files[0];
				document.getElementById('folder').innerHTML = file.webkitRelativePath.split("/")[0];
			}
			//辅助文件夹选择
			function getOtherFolderButton(){
				//file选择文件夹
				document.getElementById('otherfolder').click();
			}
			//触发file选择文件夹
			function getOtherFolder(){
				var file = document.getElementById('otherfolder').files[0];
				document.getElementById('otherfoldertext').innerHTML = file.webkitRelativePath.split("/")[0];
			}
			//执行原始图像
			function doform(){
				//获得参数
				var folder = $("#folder").text();
				var filepath=$("#filepath").text();
				nextFileName=filepath;
				
				var file = document.getElementById('getfile').files[0];
				
				//信息填写完整后执行测试
				if((folder=="")||(filepath=="")||(file==null)){
					alert("请将信息填写完整！");
				}else{
					document.getElementById("button_download_show").style.visibility = "hidden";
					document.getElementById("button_next").style.visibility = "hidden";
					
					//输入参数
					var formdata = new FormData();
					formdata.append("folder",folder);
					//formdata.append("fileFolder",filefolder);
					formdata.append("filename",filepath);
					formdata.append("file",file);
					
					
					//原始图片files
					var imagefiles = document.getElementById('imagefolder').files;
					//输入参数--原始图片files与相对路径
					for(var i=0;i<imagefiles.length;i++){
						formdata.append("imagefiles"+i,imagefiles[i]);
						formdata.append("imagepath"+i,imagefiles[i].webkitRelativePath);
					}
					formdata.append("length",imagefiles.length);
					
					//辅助文件files
					var otherfiles = document.getElementById('otherfolder').files;
					//输入参数--辅助文件files与相对路径
					for(var i=0;i<otherfiles.length;i++){
						formdata.append("otherfiles"+i,otherfiles[i]);
						formdata.append("otherpath"+i,otherfiles[i].webkitRelativePath);
					}
					formdata.append("otherlength",otherfiles.length);
					var otherfoldertext = $("#otherfoldertext").text();
					formdata.append("otherfoldertext",otherfoldertext);
					
					var sortType = $('input[type=radio][name=radio]').filter(":checked").attr("value");
					formdata.append("sortType",sortType);
					
					//设置进度条
					document.getElementById("progress-show").style.display="";
					
					//ajax调用后端
					$.ajax({
						type:"post",
						url:"sortImage",
						data:formdata,
						processData:false,
						contentType:false,
						dataType:"text",
						success:function(obj){
							excelRoute=obj;
							document.getElementById("button_download_show").style.visibility = "visible";
							document.getElementById("button_next").style.visibility = "visible";
							//取消进度条
							document.getElementById("progress-show").style.display="none";
						},
						error:function(e){
							alert("失败了"+e.status);
							//取消进度条
							document.getElementById("progress-show").style.display="none";
							document.getElementById("button_download_show").style.visibility = "hidden";
							document.getElementById("button_next").style.visibility = "hidden";
						}
					});
				}
			}
			
			//已存在实例执行测试
			function doformexsit(){
				//获得参数
				var folder = $("#folder").text();
				var exsitfile = $('input[type=radio][name=exsitfileradio]').filter(":checked").attr("value");
				if(exsitfile=="1"){
					nextFileName="Xception";
				}else if(exsitfile=="2"){
					nextFileName="VGG16";
				}else if(exsitfile=="3"){
					nextFileName="VGG19";
				}else if(exsitfile=="4"){
					nextFileName="ResNet50";
				}else if(exsitfile=="5"){
					nextFileName="MobileNet";
				}else if(exsitfile=="6"){
					nextFileName="InceptionV3";
				}else if(exsitfile=="7"){
			        nextFileName="DenseNet121";
			    }else if(exsitfile=="8"){
			        nextFileName="EfficientNet";
			    }else if(exsitfile=="9"){
			        nextFileName="InceptionResNetV2";
			    }else if(exsitfile=="10"){
			        nextFileName="NASNetMobile";
			    }
				
				//信息填写完整后执行测试
				if(folder==""){
					alert("请将信息填写完整！");
				}else{
					document.getElementById("button_download_show").style.visibility = "hidden";
					document.getElementById("button_next").style.visibility = "hidden";
					
					//输入参数
					var formdata = new FormData();
					formdata.append("folder",folder);
					
					//原始图片files
					var imagefiles = document.getElementById('imagefolder').files;
					//输入参数--原始图片files与相对路径
					for(var i=0;i<imagefiles.length;i++){
						formdata.append("imagefiles"+i,imagefiles[i]);
						formdata.append("imagepath"+i,imagefiles[i].webkitRelativePath);
					}
					formdata.append("length",imagefiles.length);
					
					var sortType = $('input[type=radio][name=radio]').filter(":checked").attr("value");
					formdata.append("sortType",sortType);
					formdata.append("exsitfile",exsitfile);
					
					//设置进度条
					document.getElementById("progress-show").style.display="";
					
					//ajax调用后端
					$.ajax({
						type:"post",
						url:"sortImageExsit",
						data:formdata,
						processData:false,
						contentType:false,
						dataType:"text",
						success:function(obj){
							excelRoute=obj;
							document.getElementById("button_download_show").style.visibility = "visible";
							document.getElementById("button_next").style.visibility = "visible";
							//取消进度条
							document.getElementById("progress-show").style.display="none";
						},
						error:function(e){
							alert("失败了"+e.status);
							//取消进度条
							document.getElementById("progress-show").style.display="none";
							document.getElementById("button_download_show").style.visibility = "hidden";
							document.getElementById("button_next").style.visibility = "hidden";
						}
					});
				}
			}
			function download(){
				javascript:location.href='fileDownload?excelRoute='+excelRoute;
			}
			function next(){
				var MR=getParameter("MR");
				var param=getParameter("param");
				var folder=$("#folder").text();
				var sortType=$('input[type=radio][name=radio]').filter(":checked").attr("value");
				var filename=nextFileName;
				var imagefiles = document.getElementById('imagefolder').files;
				var imagelength=imagefiles.length;
				var readExcelRoute=excelRoute;
				javascript:location.href='PMT.jsp?MR='+MR+"&param="+param+"&folder="+folder+"&sortType="+sortType+"&filename="+filename+"&imagelength="+imagelength+"&readExcelRoute="+excelRoute;
			}
		</script>

</head>

<body>
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
					<li><a style="color: #000000; background-color: #B0C4DE;"><span
							class="am-icon-sign-out"></span> 上传待测对象</a></li>
					<!--getProgram.jsp -->
					<li><a style="color: #000000;"><span
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
						<strong class="am-text-primary am-text-lg">
							<!-- <font size="5">执行蜕变测试</font> -->上传待测对象
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
										<p>（1）选择存放原始图像的文件夹进行上传；</p>
										<p>（2）选择原始图像优先级排序方式；</p>
										<p>（3）选择现有实例或创建待测工程，创建待测工程需要上传待测文件与依赖程序文件夹；</p>
										<p>（4）点击“执行原始图像”进行原始图像优先级排序，排序完成后页面会显示“下载排序日志”和“下一步”按钮；</p>
										<p>（5）点击“下载排序日志”获得包含原始图像优先级排序结果的excel文件；</p>
										<p>（6）点击“下一步”进入“执行测试”步骤。</p>
									</div>
								</div>
								<div class="am-panel am-panel-default admin-sidebar-panel">
									<div class="am-panel-bd">
										<p>
											<span class="am-icon-bookmark"></span> 提示
										</p>
										<p>您可以选择现有实例进行实验。</p>
									</div>
								</div>
							</div>
						</div>
						<!-- 选择原始图像文件夹与排序方式 -->
						<div class="am-panel am-panel-default">
							<div class="am-panel-hd">
								<h4 class="am-panel-title">
									<strong> <!-- <font size="5">选择蜕变关系与具体参数</font> -->选择原始图像文件夹与排序方式
									</strong>
								</h4>
							</div>
							<div class="am-panel-bd">
								<!-- 选择原始测试用例文件夹 -->
								<div class="am-g">
									<div class="am-u-lg-4">
										<input type="file" webkitdirectory mozdirectory directory
											multiple name="imagefolder" id="imagefolder"
											style="display: none" onchange="getImageFolder()">
										<button type="button"
											class="am-btn am-btn-primary am-btn-default am-btn-block"
											id="folderButton" onclick="getImageFolderButton()">
											<!-- <font size="5">浏览原始测试用例文件夹</font> -->
											浏览原始测试用例文件夹
										</button>
									</div>
									<div class="am-u-lg-8">
										<!-- <div id="folder" align="center" style="font-size:25px">undefined</div> -->
										<div id="folder" align="center"></div>
									</div>
								</div>
								<hr>
								<div class="am-g" align="center">
									<div id="radiogroup" class="am-form-group">
										<label class="am-radio-inline" id="hiddenradio1"> <input
											id="radio1" type="radio" name="radio" value="H"
											data-am-ucheck checked> <!-- <div id="radioone" style="font-size:25px">BRG</div> -->
											<div id="radioone">H</div>
										</label> <label class="am-radio-inline" id="hiddenradio2"> <input
											id="radio2" type="radio" name="radio" value="G"
											data-am-ucheck> <!-- <div id="radiotwo" style="font-size:25px">RGB</div> -->
											<div id="radiotwo">G</div>
										</label> <label class="am-radio-inline" id="hiddenradio3"> <input
											id="radio3" type="radio" name="radio" value="PMax"
											data-am-ucheck> <!-- <div id="radiothree" style="font-size:25px">RBG</div> -->
											<div id="radiothree">PMax</div>
										</label>
									</div>
								</div>
							</div>
						</div>

						<!-- 选择文件信息或现有实例 -->
						<div class="am-panel-group" id="accordion">
							<!-- 选择文件信息 -->
							<div class="am-panel am-panel-default">
								<div class="am-panel-hd">
									<h4 class="am-panel-title"
										data-am-collapse="{parent: '#accordion', target: '#uploadFilePanel'}">
										<strong> <!-- <font size="5">创建待测工程</font> -->创建待测工程
										</strong>
									</h4>
								</div>
								<div id="uploadFilePanel" class="am-panel-collapse am-collapse">
									<div class="am-panel-bd">
										<!-- 选择待测文件 -->
										<div class="am-g">
											<div class="am-u-lg-4">
												<button type="button"
													class="am-btn am-btn-primary am-btn-default am-btn-block"
													id="fileButton" onclick="getFileButton()">
													<!-- <font size="5">浏览待测程序</font> -->
													浏览待测程序
												</button>
												<input type="file" name="getfile" id="getfile"
													style="display: none" onchange="getFile()">
											</div>
											<div class="am-u-lg-8">
												<!-- <div align="center" id="filepath" style="font-size:25px">undefined</div> -->
												<div align="center" id="filepath"></div>
											</div>
										</div>
										<hr>

										<!-- 选择辅助文件夹 -->
										<div class="am-g">
											<div class="am-u-lg-4">
												<input type="file" webkitdirectory mozdirectory directory
													multiple name="otherfolder" id="otherfolder"
													style="display: none" onchange="getOtherFolder()">
												<button type="button"
													class="am-btn am-btn-primary am-btn-default am-btn-block"
													id="otherfolderButton" onclick="getOtherFolderButton()">
													<!-- <font size="5">浏览依赖程序文件夹</font> -->
													浏览依赖程序文件夹
												</button>
											</div>
											<div class="am-u-lg-8">
												<!-- <div id="otherfoldertext" align="center" style="font-size:25px">undefined</div> -->
												<div id="otherfoldertext" align="center"></div>
											</div>
										</div>
										<hr>

										<!-- 执行按钮 -->
										<div class="am-g" align="center">
											<button type="button"
												class="am-btn am-btn-primary am-btn-default am-btn-block"
												id="testButton" onclick="doform()" style="width: 50%">
												<!-- <font size="5">开始测试</font> -->
												执行原始图像
											</button>
										</div>
									</div>
								</div>
							</div>

							<!-- 选择现有实例 -->
							<div class="am-panel am-panel-default">
								<div class="am-panel-hd">
									<h4 class="am-panel-title"
										data-am-collapse="{parent: '#accordion', target: '#selectExamplePanel'}">
										<strong> <!-- <font size="5">选择现有实例</font> -->选择现有实例
										</strong>
									</h4>
								</div>
								<div id="selectExamplePanel"
									class="am-panel-collapse am-collapse am-in">
									<div class="am-panel-bd">
										<!-- 选择实例 -->
										<div class="am-g" align="center">
											<div id="exsitfilegroup" class="am-form-group"
												style="width: 35%">
												<label class="am-radio"> <input id="exsitfileradio1"
													type="radio" name="exsitfileradio" value="1" data-am-ucheck
													checked>
													<div id="exsitfileradioone" style="font-size: 1.6rem">Xception</div>
												</label> <label class="am-radio"> <input
													id="exsitfileradio2" type="radio" name="exsitfileradio"
													value="2" data-am-ucheck>
													<div id="exsitfileradiotwo" style="font-size: 1.6rem">VGG16</div>
												</label> <label class="am-radio"> <input
													id="exsitfileradio3" type="radio" name="exsitfileradio"
													value="3" data-am-ucheck>
													<div id="exsitfileradiothree" style="font-size: 1.6rem">VGG19</div>
												</label> <label class="am-radio"> <input
													id="exsitfileradio4" type="radio" name="exsitfileradio"
													value="4" data-am-ucheck>
													<div id="exsitfileradiofour" style="font-size: 1.6rem">ResNet50</div>
												</label> <label class="am-radio"> <input
													id="exsitfileradio5" type="radio" name="exsitfileradio"
													value="5" data-am-ucheck>
													<div id="exsitfileradiofive" style="font-size: 1.6rem">MobileNet</div>
												</label> <label class="am-radio"> <input
													id="exsitfileradio6" type="radio" name="exsitfileradio"
													value="6" data-am-ucheck>
													<div id="exsitfileradiosix" style="font-size: 1.6rem">InceptionV3</div>
												</label><label class="am-radio"> 
										            <input id="exsitfileradio7" type="radio" name="exsitfileradio" 
										            value="7" data-am-ucheck>
										            <div id="exsitfileradioseven" style="font-size: 1.6rem">DenseNet121</div>
										        </label>
										        <label class="am-radio"> 
										            <input id="exsitfileradio8" type="radio" name="exsitfileradio" 
										            value="8" data-am-ucheck>
										            <div id="exsitfileradioeight" style="font-size: 1.6rem">EfficientNet</div>
										        </label>
										        <label class="am-radio"> 
										            <input id="exsitfileradio9" type="radio" name="exsitfileradio" 
										            value="9" data-am-ucheck>
										            <div id="exsitfileradionine" style="font-size: 1.6rem">InceptionResNetV2</div>
										        </label>
										        <label class="am-radio"> 
										            <input id="exsitfileradio10" type="radio" name="exsitfileradio" 
										            value="10" data-am-ucheck>
										            <div id="exsitfileradioten" style="font-size: 1.6rem">NASNetMobile</div>
												</label>
											</div>
										</div>
										<hr>

										<!-- 执行按钮 -->
										<div class="am-g" align="center">
											<button type="button"
												class="am-btn am-btn-primary am-btn-default am-btn-block"
												id="testExsitButton" onclick="doformexsit()"
												style="width: 50%">执行原始图像</button>
										</div>
									</div>
								</div>
							</div>
						</div>
						<!-- 执行进度条 -->
						<div id="progress-show"
							class="am-progress am-progress-striped am-active"
							style="display: none">
							<div id="progress" class="am-progress-bar" style="width: 100%"></div>
						</div>

						<!-- 下载日志 -->
						<div class="am-g">
							<div id="button_download_show" class="am-u-lg-6" align="center"
								style="visibility: hidden">
								<button type="button" class="am-btn am-btn-primary am-btn-block"
									name="button_download" id="button_download"
									onclick="download()" style="width: 50%">
									<!-- <font size="5">下载测试日志</font> -->
									下载排序日志
								</button>
							</div>
							<div id="button_next" class="am-u-lg-6" align="center"
								style="visibility: hidden">
								<button type="button" class="am-btn am-btn-primary am-btn-block"
									name="button_PMT" id="button_PMT" onclick="next()"
									style="width: 50%">
									<!-- <font size="5">下载测试日志</font> -->
									下一步
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