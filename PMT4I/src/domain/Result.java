package domain;

import java.io.Serializable;
import java.util.Arrays;

public class Result implements Serializable {
	private String time;
	private int mr;
	private int param;
	private String probabilisticType;
	private String sortType;
	private String fileName;
	private int allNum;
	private int errorNum;
	private ImageResult[] imageResults;
	public String getTime() {
		return time;
	}
	public void setTime(String time) {
		this.time = time;
	}
	public int getMr() {
		return mr;
	}
	public void setMr(int mr) {
		this.mr = mr;
	}
	public int getParam() {
		return param;
	}
	public void setParam(int param) {
		this.param = param;
	}
	public String getProbabilisticType() {
		return probabilisticType;
	}
	public void setProbabilisticType(String probabilisticType) {
		this.probabilisticType = probabilisticType;
	}
	public String getSortType() {
		return sortType;
	}
	public void setSortType(String sortType) {
		this.sortType = sortType;
	}
	public String getFileName() {
		return fileName;
	}
	public void setFileName(String fileName) {
		this.fileName = fileName;
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
	public ImageResult[] getImageResults() {
		return imageResults;
	}
	public void setImageResults(ImageResult[] imageResults) {
		this.imageResults = imageResults;
	}
	@Override
	public String toString() {
		return "Result [time=" + time + ", mr=" + mr + ", param=" + param + ", probabilisticType=" + probabilisticType
				+ ", sortType=" + sortType + ", fileName=" + fileName + ", allNum=" + allNum + ", errorNum=" + errorNum
				+ ", imageResults=" + Arrays.toString(imageResults) + "]";
	}
	
	
	
	
	
	

}
