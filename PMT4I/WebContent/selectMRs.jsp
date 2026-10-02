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
<title>Welcome PMT4I!</title>

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

<script type="text/javascript">
			//初始化
			function start(){
				getMR();
				var imagenew = document.getElementById("image2");
				var imageold = document.getElementById("image1");
				imagenew.style.visibility = "hidden";
				imageold.style.visibility = "hidden";
			}
		
			//具体参数改变时触发
			$(document).ready(function(){
				$('input[type=radio][name=radio]').change(function(){
					form();
				});
			});
			//点击“浏览图片”
			function getImageButton(){
				//触发file选择
				document.getElementById('getImage').click();
				/*$.ajax({
					type:"post",
					url:"selectImage",
					data:"",
					dataType:"text",
					success:function(obj){
						if(obj!=""){
							document.getElementById("imagename").innerHTML = obj;
							document.getElementById("image1").src = "assets/image/old.jpg?"+new Date();
							form();
						}
					},
					error:function(e){
						alert("失败了"+e.status);
					}
				});*/
			}
			//选择图片
			function getImage(){
				/*var imagepath = document.getElementById('getImage').value;
				document.getElementById("imagename").innerHTML = imagepath;
				document.getElementById("image1").src = imagepath;
				form();*/
				
				//展示图片名称，调用form生成衍生图片
				var image = document.getElementById('getImage').files[0];
				document.getElementById("imagename").innerHTML = image.name;
				
				//展示原始图片
				var regexImageFiler=/^(?:image\/bmp|image\/png|image\/jpeg|image\/jpg|\/gif)$/i;
				var imgReader=new FileReader();
				imgReader.onload=function(evt){
					$("#image1").attr("src",evt.target.result);
				};
				var imgFile=$("#getImage").prop("files")[0];
				if(!regexImageFiler.test(imgFile.type)){
					alert("请选择有效图片！");
				}else{
					imgReader.readAsDataURL(imgFile);
					document.getElementById("image1").style.visibility = "visible";
					
					//展示衍生图片
					form();
				}
			}
			/*function getPath() {
				var obj = document.getElementById('getImage');
				if(obj) {
					if (window.navigator.userAgent.indexOf("MSIE")>=1) {
						obj.select();
				        //obj.blur();
				        //window.parent.document.body.focus();
				        return document.selection.createRange().text;
				        }
					else if(window.navigator.userAgent.indexOf("Firefox")>=1){
				    	if(obj.files) {
				    		return obj.files.item(0).getAsDataURL();
				        }
				    	return obj.value;
				    	}
					return obj.value;
				}
			}*/
			//更改MR
			function getMR(){
				//获得MR
				var MR = $("#MR").val();
				//修改可选的具体参数
				var s = ["","","","",""];
				var n = ["95%","90%","85%","80%","75%"];
				if(MR==0){
					s[0]=s[1]=s[2]=s[3]=s[4]="";
					n[0]="95%";n[1]="90%";n[2]="85%";n[3]="80%";n[4]="75%";
				}else if(MR==1){
					s[0]=s[1]=s[2]=s[3]=s[4]="";
					n[0]="5";n[1]="10";n[2]="15";n[3]="20";n[4]="25";
				}else if(MR==2){
					s[2]="";s[0]=s[1]=s[3]=s[4]="none";
					n[2]="1";n[0]=n[1]=n[3]=n[4]="";
				}else if(MR==3 || MR==4 || MR==6 || MR==7){
					s[0]=s[1]=s[2]=s[3]=s[4]="";
					n[0]="0.01";n[1]="0.02";n[2]="0.03";n[3]="0.04";n[4]="0.05";
				}else if(MR==5 || MR==8 || MR==9 || MR==10 || MR==11){
					s[0]=s[1]=s[2]=s[3]=s[4]="";
					n[0]="1.6°";n[1]="1.8°";n[2]="2.0°";n[3]="2.2°";n[4]="2.4°";
				}
				
				
				document.getElementById("hiddenradio1").style.display = s[0];
				document.getElementById("hiddenradio2").style.display = s[1];
				document.getElementById("hiddenradio3").style.display = s[2];
				document.getElementById("hiddenradio4").style.display = s[3];
				document.getElementById("hiddenradio5").style.display = s[4];
				document.getElementById("radioone").innerHTML = n[0];
				document.getElementById("radiotwo").innerHTML = n[1];
				document.getElementById("radiothree").innerHTML = n[2];
				document.getElementById("radiofour").innerHTML = n[3];
				document.getElementById("radiofive").innerHTML = n[4];
				document.getElementById("radio3").checked = true;
				//调用form生成衍生图片
				form();
			}
			//生成衍生图片，刷新图片显示
			function form(){
				var imagepath = $("#imagename").text();
				var MR = $("#MR").val();
				var param = $('input[type=radio][name=radio]').filter(":checked").attr("value");
				//如果原始图片已选择，则生成新的衍生图片
				if(imagepath==""){
					
				}else{
					var imagenew = document.getElementById("image2");
					imagenew.style.visibility = "hidden";
					document.getElementById("waitimage").innerHTML = "衍生图片-等待刷新";
					document.getElementById("imagewait").style.visibility = "visible";
					var file = document.getElementById('getImage').files[0];
					var formdata = new FormData();
					formdata.append("file",file);
					formdata.append("MR",MR);
					formdata.append("param",param);
					//ajax调用后端
					/*$.ajax({
						type:"post",
						url:"getOldImage",
						data:formdata,
						processData:false,
						contentType:false,
						dataType:"text",
						success:function(obj){
							//刷新图片显示
							var imageold = document.getElementById("image1");
							imageold.style.visibility = "visible";
							imageold.src = "assets/image/old.jpg?"+new Date();
						},
						error:function(e){
							alert("失败了"+e.status);
							document.getElementById("waitimage").innerHTML = "衍生图片";
							document.getElementById("imagewait").style.visibility = "hidden";
						}
					});*/
					$.ajax({
						type:"post",
						url:"getNewImage",
						data:formdata,
						processData:false,
						contentType:false,
						dataType:"text",
						success:function(obj){
							//刷新图片显示
							
							var imagenew = document.getElementById("image2");
							var imageold = document.getElementById("image1");
							imagenew.style.visibility = "visible";
							imageold.style.visibility = "visible";
							imagenew.src = "assets/imageshow/new.jpg?"+new Date();
							//imageold.src = "assets/image/old.jpg?"+new Date();
							document.getElementById("waitimage").innerHTML = "衍生图片";
							document.getElementById("imagewait").style.visibility = "hidden";
						},
						error:function(e){
							alert("衍生图像生成失败-"+e.status);
							document.getElementById("waitimage").innerHTML = "衍生图片";
							document.getElementById("imagewait").style.visibility = "hidden";
						}
					});
				}
			}
			function next(){
				var MR = $("#MR").val();
				var param = $('input[type=radio][name=radio]').filter(":checked").attr("value");
				javascript:location.href='getProgram.jsp?MR='+MR+"&param="+param;
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
					<li><a style="color: #000000; background-color: #B0C4DE;"><span
							class="am-icon-sign-out"></span> 选择蜕变关系</a></li>
					<!--selectMRs.jsp -->
					<li><a style="color: #000000;"><span
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
						<strong class="am-text-primary am-text-lg"> <!-- <font size="5">蜕变关系效果展示</font> -->选择蜕变关系
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
										<p>（1）通过页面选择测试使用的蜕变关系；</p>
										<p>（2）同时可以选择图像实例，页面将展示出原始图像与衍生图像的效果；</p>
										<p>（3）点击“下一步”进入“上传待测对象”步骤。</p>
									</div>
								</div>
							</div>
						</div>
						<!-- 选择效果演示图片 -->
						<div class="am-panel am-panel-default">
							<div class="am-panel-hd">
								<h4 class="am-panel-title">
									<strong> <!-- <font size="5">选择效果演示图片</font> -->选择效果演示图片
									</strong>
								</h4>
							</div>
							<div class="am-panel-bd">
								<div class="am-g">
									<div class="am-u-lg-4">
										<button type="button"
											class="am-btn am-btn-primary am-btn-default am-btn-block"
											id="imageButton" onclick="getImageButton()">
											<!-- <font size="5">浏览图片</font> -->
											浏览图片
										</button>
										<input type="file" name="getImage" id="getImage"
											style="display: none" onchange="getImage()">
									</div>
									<div class="am-u-lg-8">
										<!-- <div id="imagename" align="center" style="font-size:25px">undefined</div> -->
										<div id="imagename" align="center"></div>
									</div>
								</div>
							</div>
						</div>

						<!-- 选择蜕变关系与具体参数 -->
						<div class="am-panel am-panel-default">
							<div class="am-panel-hd">
								<h4 class="am-panel-title">
									<strong> <!-- <font size="5">选择蜕变关系与具体参数</font> -->选择蜕变关系与具体参数
									</strong>
								</h4>
							</div>
							<div class="am-panel-bd">
								<div class="am-g" align="center">
									<!-- <select id="MR" name="MR" data-am-selected="{btnWidth:'60%', btnSize: 'xl', btnStyle: 'primary'}" onchange="getMR()"> -->
									<select id="MR" name="MR"
										data-am-selected="{btnWidth:'60%', btnStyle: 'primary'}"
										onchange="getMR()">
										<option value="0" selected>1：改变对比度</option>
										<option value="1">2：改变亮度</option>
										<option value="2">3：噪声处理</option>
										<option value="3">4：仿射变换</option>
										<option value="4">5：微小平移</option>
										<option value="5">6：微小旋转</option>
										<option value="6">7：微小放大</option>
										<option value="7">8：微小缩小</option>
										<option value="8">9：模糊处理+微小旋转</option>
										<option value="9">10：改变锐度+微小旋转</option>
										<option value="10">11：微小侵蚀+微小旋转</option>
										<option value="11">12：微小膨胀+微小旋转</option>
									</select>
								</div>
								<hr>
								<div class="am-g" align="center">
									<div id="radiogroup" class="am-form-group">
										<label class="am-radio-inline" id="hiddenradio1"> <input
											id="radio1" type="radio" name="radio" value="1"
											data-am-ucheck> <!-- <div id="radioone" style="font-size:25px">BRG</div> -->
											<div id="radioone">95%</div>
										</label> <label class="am-radio-inline" id="hiddenradio2"> <input
											id="radio2" type="radio" name="radio" value="2"
											data-am-ucheck> <!-- <div id="radiotwo" style="font-size:25px">RGB</div> -->
											<div id="radiotwo">90%</div>
										</label> <label class="am-radio-inline" id="hiddenradio3"> <input
											id="radio3" type="radio" name="radio" value="3"
											data-am-ucheck checked> <!-- <div id="radiothree" style="font-size:25px">RBG</div> -->
											<div id="radiothree">85%</div>
										</label> <label class="am-radio-inline" id="hiddenradio4"> <input
											id="radio4" type="radio" name="radio" value="4"
											data-am-ucheck> <!-- <div id="radiofour" style="font-size:25px">GBR</div> -->
											<div id="radiofour">80%</div>
										</label> <label class="am-radio-inline" id="hiddenradio5"> <input
											id="radio5" type="radio" name="radio" value="5"
											data-am-ucheck> <!-- <div id="radiofive" style="font-size:25px">GRB</div> -->
											<div id="radiofive">75%</div>
										</label>
									</div>
								</div>
							</div>
						</div>

						<!-- 原始图片显示 -->
						<div class="am-u-lg-6">
							<div class="am-panel am-panel-default">
								<div class="am-panel-hd">
									<h4 class="am-panel-title">
										<!-- <strong style="font-size:25px"> 原始图片</strong> -->
										<strong> 原始图片</strong>
									</h4>
								</div>
								<div class="am-panel-bd">
									<div class="am-g" align="center">
										<img id="image1" src=""
											class="am-img-thumbnail am-img-responsive"
											style="height: 400px">
									</div>
								</div>
							</div>
						</div>
						<!-- 衍生图片显示 -->
						<div class="am-u-lg-6">
							<div class="am-panel am-panel-default">
								<div class="am-panel-hd">
									<h4 class="am-panel-title">
										<!-- <strong id="waitimage" style="font-size:25px"> 衍生图片</strong> -->
										<strong id="waitimage"> 衍生图片</strong><img id="imagewait"
											src="assets/image/wait.gif" class=""
											style="visibility: hidden">
									</h4>
								</div>
								<div class="am-panel-bd">
									<div class="am-g" align="center">
										<img id="image2" src=""
											class="am-img-thumbnail am-img-responsive"
											style="height: 400px">
									</div>
								</div>
							</div>
						</div>
						<!-- 下一步 -->
						<div id="button_next" class="am-u-lg-12" align="center">
							<button type="button" class="am-btn am-btn-primary am-btn-block"
								name="button_getProgram" id="button_getProgram" onclick="next()"
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


	<a href="#"
		class="am-icon-btn am-icon-th-list am-show-sm-only admin-menu"
		data-am-offcanvas="{target: '#admin-offcanvas'}"></a>
</body>
</html>