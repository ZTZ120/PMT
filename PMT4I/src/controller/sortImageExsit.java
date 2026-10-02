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
 * Servlet implementation class sortImageExsit
 */
@WebServlet("/sortImageExsit")
@MultipartConfig
public class sortImageExsit extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public sortImageExsit() {
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
		//getParameter���ajax�������
		String sortType=request.getParameter("sortType");
		String exsitfile=request.getParameter("exsitfile");
		//p--��Ŀ��ǰλ��
		String p = request.getSession().getServletContext().getRealPath("");
						
		//ԭʼͼ���ļ���
		String folder2=request.getParameter("folder");
		String folder=p+"assets/python/"+folder2;
						
		//�Ѵ���ͬ�����ļ�����ɾ��
		File f=new File(folder);
		if(f.exists()==true){
			deleteDir(f);
		}
		//����ԭʼͼƬ�ļ��������ļ�������ԭ·��
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
						
		//�������ʵ�������ļ�·��
		String filename;
		String objectProgram;
		if(exsitfile.equals("1")){
			filename="Xception";
			objectProgram=p+"Examples/Xception.py";
		}else if(exsitfile.equals("2")){
			filename="VGG16";
			objectProgram=p+"Examples/VGG16.py";
		}else if(exsitfile.equals("3")){
			filename="VGG19";
			objectProgram=p+"Examples/VGG19.py";
		}else if(exsitfile.equals("4")){
			filename="ResNet50";
			objectProgram=p+"Examples/ResNet50.py";
		}else if(exsitfile.equals("5")){
			filename="MobileNet";
			objectProgram=p+"Examples/MobileNet.py";
		}else{
			filename="InceptionV3";
			objectProgram=p+"Examples/InceptionV3.py";
		}
		//��ȡ�����ļ�
		InputStream is = sortImage.class.getClassLoader().getResourceAsStream("config.properties");
		Properties pp = new Properties();
		pp.load(is);
		String pythonStr = pp.getProperty("pythonstr");
		//���ñ���python������ָ��python�ļ�
		//String pythonstr = "E:\\anaconda3\\envs\\python\\python.exe";
		//String pythonstr = "D:\\beike\\Anaconda3\\envs\\python\\python.exe";
		//�Ʒ���������
		//String pythonstr = "/usr/bin/python3.6";
		//String p = request.getSession().getServletContext().getRealPath("");
		String pythonFile = p+"assets/tool/get_sort_source_image.py";
				    	
		//windows·��/����\\
		String folder1 = folder.replace('\\','/');
		String objectProgram1 = objectProgram.replace('\\','/');
				
		//excelRoute
		SimpleDateFormat sdf=new SimpleDateFormat("yyyyMMddHHmmss");
		String date=sdf.format(new Date());
		String excelRoute=p+"assets/sortexcel/"+date+"_sort_"+sortType+"_"+filename+".xls";
				    	
		//System.out.println(pythonStr+"#"+pythonFile+"#"+folder1+"#"+sortType+"#"+excelRoute+"#"+objectProgram1);
				    	
		//ִ��
		//������ִ�У�ָ��ִ���ļ�����Ӳ���
		String[]cmdArr = new String[]{pythonStr,pythonFile,"--image_folder_route",folder1,"--sort_type",sortType,"--excel_route",excelRoute,"--object_program",objectProgram1};
		Process process;
		process = Runtime.getRuntime().exec(cmdArr);


		while((new File(excelRoute)).exists()==false){
			
		}
						
		PrintWriter out=response.getWriter();
		out.write(excelRoute);
		out.close();
	}
	//ɾ���ļ���
	private static void deleteDir(File dir){
		//ɾ���ļ���
		if(dir.isDirectory()){
			String[] children = dir.list();
			for(int i=0;i<children.length;i++){
				deleteDir(new File(dir,children[i]));
			}
		}
			
		//ɾ���ļ�
		dir.delete();
	}
}
