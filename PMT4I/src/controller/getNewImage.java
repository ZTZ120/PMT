package controller;

import java.io.ByteArrayOutputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;

/**
 * Servlet implementation class getNewImage
 */
@WebServlet("/getNewImage")
@MultipartConfig
public class getNewImage extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public getNewImage() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doPost(request, response);
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		//getParameter获得ajax传入参数
		//String imagepath=request.getParameter("imagepath");
				
		//p--项目当前位置
		String p = request.getSession().getServletContext().getRealPath("");
				
		//原始图片保存路径
		String imagePath = p+"assets/imageshow/old.jpg";
		File imageFile1 = new File(imagePath);
		if(imageFile1.exists()==true){
			imageFile1.delete();
		}
		
		Part part=request.getPart("file");
		part.write(imagePath);
				
		//getParameter获得ajax传入参数
		int MR=Integer.valueOf(request.getParameter("MR"))+1;
		String param=request.getParameter("param");
		//衍生图片保存路径
		String newImagePath = p+"assets/imageshow/new.jpg";
				
		//读取配置文件
		InputStream is = getNewImage.class.getClassLoader().getResourceAsStream("config.properties");
		Properties pp = new Properties();
		pp.load(is);
		String pythonStr = pp.getProperty("pythonstr");
		//调用本地python环境
		//String pythonstr = "E:\\anaconda3\\envs\\python\\python.exe";
		//String pythonstr = "D:\\beike\\Anaconda3\\envs\\python\\python.exe";
		//云服务器更改
		//String pythonstr = "/usr/bin/python3.6";
		//String p = request.getSession().getServletContext().getRealPath("");
		    	
		//调用python文件
		String pythonFile = p+"assets/tool/get_follow_image.py";
		    	
		//windows路径/或者\\
		imagePath = imagePath.replace('\\','/');
		newImagePath = newImagePath.replace('\\', '/');
		    	
		//获取衍生图像修改时间
		long lastModifiedTime1=(new File(newImagePath)).lastModified();
		//执行
		//System.out.println(pythonStr+" "+pythonFile+" "+imagePath+" "+newImagePath+" "+MR+" "+param);
		//命令行执行，指定执行文件，添加参数
		String[]cmdArr = new String[]{pythonStr,pythonFile,"--source_image_route",imagePath,"--follow_image_route",newImagePath,"--MR",String.valueOf(MR),"--param",param};
		Process process;
		process = Runtime.getRuntime().exec(cmdArr);
		while((new File(newImagePath)).lastModified()==lastModifiedTime1){
			
		}
	}

}
