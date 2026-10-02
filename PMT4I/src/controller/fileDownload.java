package controller;

import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.OutputStream;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class fileDownload
 */
@WebServlet("/fileDownload")
public class fileDownload extends HttpServlet {
	private static final long serialVersionUID = 1L;
	private static final String CONTENT_TYPE = "text/html; charset=GBK";
       
    /**
     * @see HttpServlet#HttpServlet()
     */
    public fileDownload() {
        super();
        // TODO Auto-generated constructor stub
    }

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		response.setContentType(CONTENT_TYPE);

		//p--项目当前位置
		String p = request.getSession().getServletContext().getRealPath("");
		String excelRoute = request.getParameter("excelRoute");
        //创建file对象
        File file=new File(excelRoute);//下载的日志文件名

        //设置response的编码方式
        response.setContentType("application/x-msdownload");

        //写明要下载的文件的大小
        response.setContentLength((int)file.length());

        //解决中文乱码
        response.setHeader("Content-Disposition","attachment; filename="+excelRoute);       

        //读出文件到i/o流
        FileInputStream fis=new FileInputStream(file);
        BufferedInputStream buff=new BufferedInputStream(fis);

        byte [] b=new byte[1024];//相当于我们的缓存

        long k=0;//该值用于计算当前实际下载了多少字节

        //从response对象中得到输出流,准备下载

        OutputStream myout=response.getOutputStream();

        //开始循环下载

        while(k<file.length()){

            int j=buff.read(b,0,1024);
            k+=j;

            //将b中的数据写到客户端的内存
            myout.write(b,0,j);

        }

        //将写入到客户端的内存的数据,刷新到磁盘
        myout.flush();
        System.out.println("下载完成");
	}

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		// TODO Auto-generated method stub
		doGet(request, response);
	}

}
