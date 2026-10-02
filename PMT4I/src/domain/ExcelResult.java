package domain;

import java.io.Serializable;

public class ExcelResult implements Serializable {
	private String excelRoute;
	private int allNum;
	private int errorNum;
	public String getExcelRoute() {
		return excelRoute;
	}
	public void setExcelRoute(String excelRoute) {
		this.excelRoute = excelRoute;
	}
	public int getAllNum() {
		return allNum;
	}
	public void setAllNum(int allNum) {
		this.allNum = allNum;
	}
	public int getErrorNum() {
		return errorNum;
	}
	public void setErrorNum(int errorNum) {
		this.errorNum = errorNum;
	}
	@Override
	public String toString() {
		return "ExcelResult [excelRoute=" + excelRoute + ", allNum=" + allNum + ", errorNum=" + errorNum + "]";
	}
	
}
