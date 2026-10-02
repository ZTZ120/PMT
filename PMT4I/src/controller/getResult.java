package controller;

import java.io.File;
import java.io.IOException;
import javax.servlet.ServletException;
import javax.servlet.annotation.MultipartConfig;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import com.fasterxml.jackson.databind.ObjectMapper;

import domain.ExcelResult;
import domain.ImageResult;
import domain.Result;
import jxl.Sheet;
import jxl.Workbook;
import jxl.read.biff.BiffException;

/**
 * Servlet implementation class getResult
 */
@WebServlet("/getResult")
@MultipartConfig
public class getResult extends HttpServlet {
	private static final long serialVersionUID = 1L;
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public getResult() {
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
		String excelRoute=request.getParameter("excelRoute");
		//∂¡»°excel
		Result result=new Result();
		Workbook book=null;
		try {
			book = Workbook.getWorkbook(new File(excelRoute));
		} catch (BiffException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		Sheet sheet=book.getSheet(0);
		String time=sheet.getCell(0, 1).getContents();
		String mr=sheet.getCell(2, 1).getContents();
		String param=sheet.getCell(3, 1).getContents();
		String probabilisticType=sheet.getCell(4, 1).getContents();
		String sortType=sheet.getCell(5, 1).getContents();
		String fileName=sheet.getCell(1, 1).getContents();
		int rows=sheet.getRows();
		int errorrows=0;
		ImageResult[] imageResults=new ImageResult[rows-1];
		for(int r=1;r<rows;r++){
			String path=sheet.getCell(6, r).getContents();
			String PMT=sheet.getCell(7, r).getContents();
			if(PMT.equals("0")){
				errorrows++;
			}
			ImageResult imageResult=new ImageResult();
			imageResult.setPath(path);
			imageResult.setResultType(Integer.valueOf(PMT));
			imageResults[r-1]=imageResult;
		}
		//–¥result
		result.setTime(time);
		result.setMr(Integer.valueOf(mr));
		result.setParam(Integer.valueOf(param));
		result.setProbabilisticType(probabilisticType);
		result.setSortType(sortType);
		result.setFileName(fileName);
		result.setAllNum(rows-1);
		result.setErrorNum(errorrows);
		result.setImageResults(imageResults);
		ObjectMapper mapper = new ObjectMapper();
        response.setContentType("application/json;charset=utf-8");
        mapper.writeValue(response.getOutputStream(),result);
	}

}
