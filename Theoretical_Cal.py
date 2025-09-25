#Theoretical = C * (log n * log log n)
import math

def calculate_and_save_theoretical_times(C, lines):
    """
    使用计算出的常数C，计算results.txt中所有n值的理论时间并保存到新文件
    
    参数:
    C: 计算出的常数
    lines: results.txt的所有行
    """
    print(f"\n使用常数 C = {C:.6e} 计算所有n值的理论时间:")
    print("="*60)
    
    # 准备保存理论时间的数据
    theoretical_results = []
    theoretical_results.append("Project 1 - Theoretical Time Results")
    theoretical_results.append("="*40)
    theoretical_results.append("N\t\tTheoretical Time (seconds)")
    theoretical_results.append("-"*40)
    
    # 查找并处理所有数据行
    for line in lines:
        line = line.strip()
        # 查找包含科学计数法格式数据的行
        if 'e+' in line or 'e-' in line:
            try:
                parts = line.split()
                n = float(parts[0])  # N值
                
                # 计算理论时间
                log_n = math.log(n)
                log_log_n = math.log(log_n)
                theoretical_time = C * (log_n * log_log_n)
                
                # 格式化输出和保存
                n_str = f"{n:.3e}"
                time_str = f"{theoretical_time:.6e}"
                
                print(f"N = {n_str}\t理论时间 = {time_str}")
                theoretical_results.append(f"{n_str}\t{time_str}")
                
            except (ValueError, IndexError) as e:
                print(f"解析行时出错: {line}, 错误: {e}")
                continue
    
    # 添加注释
    theoretical_results.append("-"*40)
    theoretical_results.append("Note: Theoretical times calculated using formula C * (log n * log log n)")
    theoretical_results.append(f"Where C = {C:.6e}")
    theoretical_results.append("")
    
    # 保存到文件
    try:
        with open('theoretical_results.txt', 'w') as file:
            for line in theoretical_results:
                file.write(line + '\n')
        print(f"\n理论时间结果已保存到 'theoretical_results.txt'")
    except Exception as e:
        print(f"保存文件时出错: {e}")

def calculate_C_from_results(data_row_index=0):
    """
    从results.txt文件中读取指定行的n值及其结果，然后计算出常数C的值
    
    参数:
    data_row_index: 要使用的数据行索引 (0表示第一行数据，1表示第二行数据，以此类推)
    
    返回:
    C: 计算出的常数
    """
    try:
        # 读取results.txt文件
        with open('results.txt', 'r') as file:
            lines = file.readlines()
        
        # 查找所有数据行（跳过标题和分隔线）
        data_lines = []
        for line in lines:
            line = line.strip()
            # 查找包含科学计数法格式数据的行
            if 'e+' in line or 'e-' in line:
                data_lines.append(line)
        
        if not data_lines:
            raise ValueError("未找到有效的数据行")
        
        # 检查索引是否有效
        if data_row_index < 0 or data_row_index >= len(data_lines):
            print(f"警告: 数据行索引 {data_row_index} 超出范围 (0-{len(data_lines)-1})")
            print(f"使用第一行数据 (索引 0)")
            data_row_index = 0
        
        # 获取指定的数据行
        data_line = data_lines[data_row_index]
        
        # 解析数据行，分割N值和时间
        parts = data_line.split()
        n = float(parts[0])  # N值
        measured_time = float(parts[1])  # 时间值
        
        print(f"从results.txt读取的数据 (第 {data_row_index + 1} 行数据):")
        print(f"N = {n}")
        print(f"时间 = {measured_time} 秒")
        print(f"总共有 {len(data_lines)} 行数据可选择")
        
        # 计算常数C
        log_n = math.log(n)
        log_log_n = math.log(log_n)
        
        C = measured_time / (log_n * log_log_n)
        
        print(f"\n计算过程:")
        print(f"log(n) = {log_n}")
        print(f"log(log(n)) = {log_log_n}")
        print(f"log(n) * log(log(n)) = {log_n * log_log_n}")
        
        print(f"\n计算结果:")
        print(f"常数 C = {C}")
        print(f"常数 C (科学计数法) = {C:.6e}")
        
        # 验证计算结果
        theoretical_time = C * (log_n * log_log_n)
        print(f"\n验证:")
        print(f"理论时间 = C * (log n * log log n) = {theoretical_time}")
        print(f"实测时间 = {measured_time}")
        print(f"误差 = {abs(theoretical_time - measured_time)}")
        
        # 计算所有n值的理论时间并保存
        calculate_and_save_theoretical_times(C, lines)
        
        return C
        
    except FileNotFoundError:
        print("错误: 找不到results.txt文件")
        return None
    except Exception as e:
        print(f"错误: {e}")
        return None

# 执行函数
if __name__ == "__main__":
    C = calculate_C_from_results()
    if C is not None:
        print(f"\n最终结果: 常数 C = {C:.6e}")