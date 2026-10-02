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

import com.fasterxml.jackson.databind.ObjectMapper;

import domain.ExcelResult;
import jxl.Sheet;
import jxl.Workbook;
import jxl.read.biff.BiffException;

/**
 * Servlet implementation class testMain
 */
@WebServlet("/testMain")
@MultipartConfig
public class testMain extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public testMain() {
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
		int MR=Integer.valueOf(request.getParameter("MR"))+1;
		String param=request.getParameter("param");
		String imageRows=request.getParameter("imageRows");
		String probabilisticType=request.getParameter("probabilisticType");
		String readExcelRoute=request.getParameter("readExcelRoute");
		String sortType=request.getParameter("sortType");
		//p--项目当前位置
		String p = request.getSession().getServletContext().getRealPath("");
		//读取配置文件
		InputStream is = sortImage.class.getClassLoader().getResourceAsStream("config.properties");
		Properties pp = new Properties();
		pp.load(is);
		String pythonStr = pp.getProperty("pythonstr");
		String pythonFile = p+"assets/tool/get_PMT.py";
		//excelRoute
		SimpleDateFormat sdf=new SimpleDateFormat("yyyyMMddHHmmss");
		String date=sdf.format(new Date());
		String excelRoute=p+"assets/PMTexcel/"+date+"_MR"+String.valueOf(MR)+"-"+param+"_"+probabilisticType+"_"+sortType+".xls";
		//System.out.println(excelRoute);
		//执行
		//命令行执行，指定执行文件，添加参数
		String[]cmdArr = new String[]{pythonStr,pythonFile,"--probabilistic_type",probabilisticType,"--read_excel_route",readExcelRoute,"--excel_route",excelRoute,"--image_rows",imageRows,"--MR",String.valueOf(MR),"--param",param};
		Process process;
		process = Runtime.getRuntime().exec(cmdArr);
		//System.out.println(pythonStr+" "+pythonFile+" --probabilistic_type "+probabilisticType+" --read_excel_route "+readExcelRoute+" --excel_route "+excelRoute+" --image_rows "+imageRows+" --MR "+String.valueOf(MR)+" --param "+param);
		while((new File(excelRoute)).exists()==false){
			
		}
						
		//读取图像总行数和未通过测试数量
		ExcelResult excelResult=new ExcelResult();
		Workbook book=null;
		try {
			book = Workbook.getWorkbook(new File(excelRoute));
		} catch (BiffException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		Sheet sheet=book.getSheet(0);
		int rows=sheet.getRows();
		int errorrows=0;
		for(int r=1;r<rows;r++){
			String PMT=sheet.getCell(7, r).getContents();
			if(PMT.equals("0")){
				errorrows++;
			}
		}
		excelResult.setAllNum(rows-1);
		excelResult.setExcelRoute(excelRoute);
		excelResult.setErrorNum(errorrows);
		ObjectMapper mapper = new ObjectMapper();
        response.setContentType("application/json;charset=utf-8");
        mapper.writeValue(response.getOutputStream(),excelResult);
	}

}
