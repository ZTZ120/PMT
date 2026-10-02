package domain;

import java.io.Serializable;

public class ImageResult implements Serializable {
	private String path;
	private int resultType;
	public String getPath() {
		return path;
	}
	public void setPath(String path) {
		this.path = path;
	}
	public int getResultType() {
		return resultType;
	}
	public void setResultType(int resultType) {
		this.resultType = resultType;
	}
	
	@Override
	public String toString() {
		return "ImageResult [path=" + path + ", resultType=" + resultType + "]";
	}

}
