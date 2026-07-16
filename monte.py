# 라이브러리 불러오기
import tkinter as tk
import random
import math

# 전역 변수 초기화 (다트 개수 카운트)
total_darts = 0
inside_darts = 0

# 다트를 던지고 계산하는 핵심 함수
def throw_darts(num):
    global total_darts, inside_darts
    
    for _ in range(num):
        # 가로, 세로 길이가 300 픽셀인 정사각형 과녁 안에 랜덤한 위치에 다트 던지기
        x = random.uniform(50, 350)
        y = random.uniform(50, 350)
        
        # 중심으로부터의 거리를 구해 원 안에 들어왔는지 판단
        distance = math.sqrt((x - 200)**2 + (y - 200)**2)
        
        if distance <= 150:
            inside_darts += 1
            color = "#4D96FF"  # 원 안은 파란색 점
        else:
            color = "#FF6B6B"  # 원 밖은 빨간색 점
            
        total_darts += 1
        
        # 화면(Canvas)에 아주 작은 다트 점(반지름 1) 찍기
        canvas.create_oval(x-1, y-1, x+1, y+1, fill=color, outline=color)
        
    # 수치 업데이트 계산
    # 원의 넓이(π) = 4 * (inside_darts / total_darts)
    estimated_pi = 4.0 * inside_darts / total_darts
    actual_pi = math.pi
    error = abs(actual_pi - estimated_pi)
    
    # GUI 레이블 문구 실시간 변경
    lbl_total.config(text=f"총 던진 다트 수 (N): {total_darts:,} 개")
    lbl_inside.config(text=f"원 안에 꽂힌 수 (C): {inside_darts:,} 개")
    lbl_estimated.config(text=f"몬테카를로 예측 넓이 (π): {estimated_pi:.5f}")
    lbl_actual.config(text=f"수학적 실제 원 넓이 (π): {actual_pi:.5f}")
    lbl_error.config(text=f"실제 값과의 오차 (노이즈): {error:.5f}")

# 데이터를 리셋 함수
def reset_simulation():
    global total_darts, inside_darts
    total_darts = 0
    inside_darts = 0
    canvas.delete("all")
    # 기본 틀 그리기
    canvas.create_rectangle(50, 50, 350, 350, outline="black", width=2)
    canvas.create_oval(50, 50, 350, 350, outline="gray", width=1)
    lbl_total.config(text="총 던진 다트 수 (N): 0 개")
    lbl_inside.config(text="원 안에 꽂힌 수 (C): 0 개")
    lbl_estimated.config(text="몬테카를로 적분 넓이 (π): 0.00000")
    lbl_error.config(text="실제 값과의 오차 (노이즈): 0.00000")

# GUI 레이아웃
root = tk.Tk()
root.title("미적분 수행평가-몬테카를로 적분 시뮬레이터")
root.geometry("750x450")
root.resizable(False, False)

# 좌측: 다트판이 그려질 캔버스
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack(side="left", padx=20, pady=20)

# 기본 정사각형 , 원 그리기
canvas.create_rectangle(50, 50, 350, 350, outline="black", width=2)
canvas.create_oval(50, 50, 350, 350, outline="gray", width=1)

# 우측 : 수치 표기,버튼 프레임
frame_control = tk.Frame(root)
frame_control.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# 타이틀 제목
lbl_title = tk.Label(frame_control, text="■ 실시간 데이터 분석", font=("맑은 고딕", 14, "bold"))
lbl_title.pack(anchor="w", pady=10)

# 현황 수치 레이블들
lbl_total = tk.Label(frame_control, text="총 던진 다트 수 (N): 0 개", font=("맑은 고딕", 11))
lbl_total.pack(anchor="w", pady=4)

lbl_inside = tk.Label(frame_control, text="원 안에 꽂힌 수 (C): 0 개", font=("맑은 고딕", 11))
lbl_inside.pack(anchor="w", pady=4)

div = tk.Frame(frame_control, height=2, bg="lightgray")
div.pack(fill="x", pady=10)

lbl_estimated = tk.Label(frame_control, text="몬테카를로 적분 넓이 (π): 0.00000", font=("맑은 고딕", 11, "bold"), fg="blue")
lbl_estimated.pack(anchor="w", pady=4)

lbl_actual = tk.Label(frame_control, text=f"수학적 실제 원 넓이 (π): {math.pi:.5f}", font=("맑은 고딕", 11), fg="green")
lbl_actual.pack(anchor="w", pady=4)

lbl_error = tk.Label(frame_control, text="실제 값과의 오차 (노이즈): 0.00000", font=("맑은 고딕", 11, "bold"), fg="red")
lbl_error.pack(anchor="w", pady=4)

# 제어 버튼들
btn_frame = tk.Frame(frame_control)
btn_frame.pack(side="bottom", fill="x", pady=10)

btn_100 = tk.Button(btn_frame, text="+100개 던지기", command=lambda: throw_darts(100), font=("맑은 고딕", 10))
btn_100.grid(row=0, column=0, padx=5, sticky="ew")

btn_1000 = tk.Button(btn_frame, text="+1,000개 던지기", command=lambda: throw_darts(1000), font=("맑은 고딕", 10))
btn_1000.grid(row=0, column=1, padx=5, sticky="ew")

btn_reset = tk.Button(btn_frame, text="초기화", command=reset_simulation, font=("맑은 고딕", 10), bg="lightgray")
btn_reset.grid(row=0, column=2, padx=5, sticky="ew")

btn_frame.columnconfigure(0, weight=1)
btn_frame.columnconfigure(1, weight=1)
btn_frame.columnconfigure(2, weight=1)

root.mainloop()