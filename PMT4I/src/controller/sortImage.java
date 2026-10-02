package controller;

import java.io.File;
import java.io.IOException;
import java.io.InputStream;
import java.io.PrintWriter;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Properties;

import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;


/**
 * Servlet implementation class sortImage
 */
@WebServlet("/sortImage")
@MultipartConfig
public class sortImage extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public sortImage() {
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
		String sortType=request.getParameter("sortType");
		//p--项目当前位置
		String p = request.getSession().getServletContext().getRealPath("");
				
		//原始图像文件夹
		String folder2=request.getParameter("folder");
		String folder=p+"assets/python/"+folder2;
				
		//已存在同名的文件夹则删除
		File f=new File(folder);
		if(f.exists()==true){
			deleteDir(f);
		}
		//保存原始图片文件夹所有文件，保留原路径
		//MultipartFile[] imagefiles = request.getParts("imagefiles");
		String length = request.getParameter("length");
		Part part1;
		String relativepath="";
		File imageFile;
		
		for(int i=0;i<Integer.parseInt(length);i++){
			part1=request.getPart("imagefiles"+i);
			relativepath = request.getParameter("imagepath"+i);
			imageFile = new File(p+"assets/python/"+relativepath);
			imageFile.getParentFile().mkdirs();
			part1.write(p+"assets/python/"+relativepath);
		}
				
		//辅助文件夹
		//已存在同名的文件夹则删除
		File f_other=new File(p+"assets/python/"+request.getParameter("otherfoldertext"));
		if(f_other.exists()==true){
			deleteDir(f_other);
		}
		//保存辅助文件夹所有文件，保留原路径
		String otherlength = request.getParameter("otherlength");
		Part otherpart;
		String otherrelativepath="";
		File otherFile;
		for(int i=0;i<Integer.parseInt(otherlength);i++){
			otherpart=request.getPart("otherfiles"+i);
			otherrelativepath = request.getParameter("otherpath"+i);
			otherFile = new File(p+"assets/python/"+otherrelativepath);
			otherFile.getParentFile().mkdirs();
			otherpart.write(p+"assets/python/"+otherrelativepath);
		}	
				
		//保存待测文件到指定路径
		//String fileFolder=request.getParameter("fileFolder");
		//String p = request.getSession().getServletContext().getRealPath("");
		String fileFolder = p+"assets/python";
		String filename1=request.getParameter("filename");
		int j=filename1.indexOf('.');
		String filename = filename1.substring(0,j);
		/*String[] filename2 = filename1.split(".");
		System.out.println(filename2.length);
		String filename = filename2[0];*/
		String objectProgram=fileFolder+"/"+filename1;
		//已存在的文件删除
		File f_file=new File(objectProgram);
		if(f_file.exists()==true){
			f_file.delete();
		}
		Part part=request.getPart("file");
		part.write(objectProgram);
				
		//读取配置文件
		InputStream is = sortImage.class.getClassLoader().getResourceAsStream("config.properties");
		Properties pp = new Properties();
		pp.load(is);
		String pythonStr = pp.getProperty("pythonstr");
		//调用本地python环境，指定python文件
		//String pythonstr = "E:\\anaconda3\\envs\\python\\python.exe";
		//String pythonstr = "D:\\beike\\Anaconda3\\envs\\python\\python.exe";
		//云服务器更改
		//String pythonstr = "/usr/bin/python3.6";
		//String p = request.getSession().getServletContext().getRealPath("");
		String pythonFile = p+"assets/tool/get_sort_source_image.py";
		    	
		//windows路径/或者\\
		String folder1 = folder.replace('\\','/');
		String objectProgram1 = objectProgram.replace('\\','/');
		
		//excelRoute
		SimpleDateFormat sdf=new SimpleDateFormat("yyyyMMddHHmmss");
		String date=sdf.format(new Date());
		String excelRoute=p+"assets/sortexcel/"+date+"_sort_"+sortType+"_"+filename+".xls";
		    	
		//System.out.println(pythonStr+"#"+pythonFile+"#"+folder1+"#"+sortType+"#"+excelRoute+"#"+objectProgram1);
		    	
		//执行
		//命令行执行，指定执行文件，添加参数
		String[]cmdArr = new String[]{pythonStr,pythonFile,"--image_folder_route",folder1,"--sort_type",sortType,"--excel_route",excelRoute,"--object_program",objectProgram1};
		Process process;
		process = Runtime.getRuntime().exec(cmdArr);
		
		while((new File(excelRoute)).exists()==false){
			
		}
		
		PrintWriter out=response.getWriter();
		out.write(excelRoute);
		out.close();
		
	}
	//删除文件夹
	private static void deleteDir(File dir){
		//删除文件夹
		if(dir.isDirectory()){
			String[] children = dir.list();
			for(int i=0;i<children.length;i++){
				deleteDir(new File(dir,children[i]));
			}
		}
		
		//删除文件
		dir.delete();
	}
}
