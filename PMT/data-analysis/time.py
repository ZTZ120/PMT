import xlrd
import xlwt
import scipy.stats as ss
import numpy as np
import pandas as pd

object="EfficientNet"

def dataAnalysistime():
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('mysheet', cell_overwrite_ok=False)
    read_excel_route_Pri=["/mnt/c/resultstime/"+object+"/sort_H_"+object+".xls",
                         "/mnt/c/resultstime/"+object+"/sort_G_"+object+".xls",
                         "/mnt/c/resultstime/"+object+"/sort_PMax_"+object+".xls"]
    read_excel_route_MT=["/mnt/c/resultstime/"+object+"/MR1-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR2-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR3-1_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR4-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR5-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR6-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR7-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR8-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR9-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR10-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR11-3_MT_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR12-3_MT_H.xls"]
    read_excel_route_Jaccard=["/mnt/c/resultstime/"+object+"/MR1-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR2-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR3-1_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR4-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR5-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR6-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR7-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR8-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR9-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR10-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR11-3_Jaccard_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR12-3_Jaccard_H.xls"]
    read_excel_route_Wilcoxon=["/mnt/c/resultstime/"+object+"/MR1-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR2-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR3-1_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR4-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR5-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR6-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR7-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR8-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR9-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR10-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR11-3_Wilcoxon_H.xls",
                         "/mnt/c/resultstime/"+object+"/MR12-3_Wilcoxon_H.xls"]
    # 新增：处理文件并把结果写入 sheet
    groups = [
        ("MT", read_excel_route_MT, 17),
        ("Jaccard", read_excel_route_Jaccard, 16),
        ("Wilcoxon", read_excel_route_Wilcoxon, 36),
    ]
    # 表头
    headers = ["method", "file", "API", "testcase","diff"]
    for c, h in enumerate(headers):
        sheet.write(0, c, h)

    # 初始化用于计算平均值的容器
    method_stats = {g[0]: {"API": [], "testcase": [], "diff": []} for g in groups}
    # 为 Pri 单独准备容器（只有 API 和 testcase 两列）
    method_stats["Pri"] = {"API": [], "testcase": [], "diff": []}

    row_idx = 1
    for method, paths, col_start in groups:
        for p in paths:
            try:
                df = pd.read_excel(p, header=None)
                # 使用第二行（行索引1）
                r = df.iloc[1]
                total = float(r[col_start])
                total_time = float(r[col_start + 1])
                API_time = float(r[col_start + 2])
                API_testcase = total_time + API_time
                diff = total - API_testcase
                # 写入明细
                sheet.write(row_idx, 0, method)
                sheet.write(row_idx, 1, p)
                sheet.write(row_idx, 2, total_time)
                sheet.write(row_idx, 3, API_time)
                sheet.write(row_idx, 4, diff)
                # 收集用于平均值计算
                method_stats[method]["API"].append(total_time)
                method_stats[method]["testcase"].append(API_time)
                method_stats[method]["diff"].append(diff)
            except Exception as e:
                # 如果读取或索引失败，写入错误信息并继续
                sheet.write(row_idx, 0, method)
                sheet.write(row_idx, 1, p)
                sheet.write(row_idx, 2, "ERROR")
                sheet.write(row_idx, 3, str(e))
            row_idx += 1

    # 处理 Pri（sort_H/ sort_G/ sort_PMax），使用第16列和第17列（行索引1）
    for p in read_excel_route_Pri:
        try:
            df = pd.read_excel(p, header=None)
            r = df.iloc[1]
            total_time = float(r[10])
            API_time = float(r[11])
            # Pri 没有 total 列，diff 写空
            diff=total_time-API_time
            sheet.write(row_idx, 0, "Pri")
            sheet.write(row_idx, 1, p)
            sheet.write(row_idx, 2, API_time)
            sheet.write(row_idx, 3, "")
            sheet.write(row_idx, 4, diff)
            # 收集用于平均值计算（不收集 diff）
            method_stats["Pri"]["API"].append(API_time)
            method_stats["Pri"]["diff"].append(diff)
        except Exception as e:
            sheet.write(row_idx, 0, "Pri")
            sheet.write(row_idx, 1, p)
            sheet.write(row_idx, 2, "ERROR")
            sheet.write(row_idx, 3, str(e))
        row_idx += 1


    # 写入平均值汇总（在明细之后留一行空行）
    summary_start = row_idx + 1
    sheet.write(summary_start, 0, "method")
    sheet.write(summary_start, 1, "avg_API")
    sheet.write(summary_start, 2, "avg_testcase")
    sheet.write(summary_start, 3, "avg_diff")
    summary_row = summary_start + 1

    def mean_or_none(lst):
        return float(np.mean(lst)) if len(lst) > 0 else None

    for method in method_stats:
        avg_api_raw = mean_or_none(method_stats[method]["API"])
        avg_test_raw = mean_or_none(method_stats[method]["testcase"])
        avg_diff_raw = mean_or_none(method_stats[method]["diff"])

        avg_api = avg_api_raw/1000.0 if avg_api_raw is not None else "N/A"
        avg_test = avg_test_raw/1000.0 if avg_test_raw is not None else "N/A"
        avg_diff = avg_diff_raw/1000.0 if avg_diff_raw is not None else "N/A"

        sheet.write(summary_row, 0, method)
        sheet.write(summary_row, 1, avg_api)
        sheet.write(summary_row, 2, avg_test)
        sheet.write(summary_row, 3, avg_diff)
        summary_row += 1
    
    out_path = "/mnt/c/resultstime/"+object+"/time_analysis_" + object + ".xls"
    book.save(out_path)
    return out_path

if __name__ == '__main__':
    dataAnalysistime()