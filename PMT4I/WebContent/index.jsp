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

</head>
<body>
	<!-- 编写代码 -->
	<!-- 标题 -->
	<header class="am-topbar am-topbar-inverse admin-header">
		<div class="am-topbar-brand">
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
					<li><a href="index.jsp"
						style="color: #006699; background-color: #B0C4DE;"><span
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
					<li><a style="color: #000000;"><span
							class="am-icon-sign-out"></span> 查看测试结果</a></li>
					<!--showResult.jsp -->
				</ul>
				<div class="am-panel am-panel-default admin-siderbar-panel">
					<div class="am-panel-bd">
						<p>
							<!-- <img src="assets/i/banner1.png" width="40"> -->
							<span class="am-icon-tag"></span> 欢迎
							<!-- Welcome -->
						</p>
						<p>
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
						<strong class="am-text-primary am-text-lg">使用说明</strong>
					</div>
				</div>
				<hr>

				<!-- 右侧主内容 -->
				<div class="am-g">
					<div class="am-panel am-panel-default admin-sidebar-panel">
						<div class="am-panel-bd">
							<p>
								<span class="am-icon-bookmark"></span> 开始
							</p>
							<p>（1）介绍工具使用说明；</p>
							<p>（2）工具使用入口。</p>
						</div>
						<div class="am-panel-bd">
							<p>
								<span class="am-icon-bookmark"></span> 选择蜕变关系
							</p>
							<p>（1）通过页面选择测试使用的蜕变关系；</p>
							<p>（2）同时可以选择图像实例，页面将展示出原始图像与衍生图像的效果；</p>
							<p>（3）点击“下一步”进入“上传待测对象”步骤。</p>
						</div>
						<div class="am-panel-bd">
							<p>
								<span class="am-icon-bookmark"></span> 上传待测对象
							</p>
							<p>（1）选择存放原始图像的文件夹进行上传；</p>
							<p>（2）选择原始图像优先级排序方式；</p>
							<p>（3）选择现有实例或创建待测工程，创建待测工程需要上传待测文件与依赖程序文件夹；</p>
							<p>（4）点击“执行原始图像”进行原始图像优先级排序，排序完成后页面会显示“下载排序日志”和“下一步”按钮；</p>
							<p>（5）点击“下载排序日志”获得包含原始图像优先级排序结果的excel文件；</p>
							<p>（6）点击“下一步”进入“执行测试”步骤。</p>
						</div>
						<div class="am-panel-bd">
							<p>
								<span class="am-icon-bookmark"></span> 执行测试
							</p>
							<p>（1）填写需要使用的原始图像数量；</p>
							<p>（2）选择测试方法；</p>
							<p>（3）点击“开始测试”执行测试方法，测试结束后页面会展示测试图像总数量、未通过测试的图像数量和未通过测试比率，同时页面显示出“下载测试日志”和“查看测试结果”按钮；</p>
							<p>（4）点击“下载测试日志”获得包含测试结果的excel文件；</p>
							<p>（5）点击“查看测试结果”进入“查看测试结果”步骤。</p>
						</div>
						<div class="am-panel-bd">
							<p>
								<span class="am-icon-bookmark"></span> 查看测试结果
							</p>
							<p>（1）页面展示详细测试结果。</p>
						</div>
					</div>
					<!-- 下一步 -->
					<div id="button_next" class="am-u-lg-12" align="center">
						<button type="button" class="am-btn am-btn-primary am-btn-block"
							name="button_selectMRs" id="button_selectMRs"
							onclick="javascript:location.href='selectMRs.jsp'"
							style="width: 50%">
							<!-- <font size="5">下载测试日志</font> -->
							开始
						</button>
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