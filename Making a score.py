from colorama import init, Fore, Style
init(autoreset=True)

# ------------------------------
# بخش Homework
# ------------------------------
homework = int(input(Fore.CYAN + "How many homework do you have? "))
test_homework = 0  # جمع نمره‌های Homework

for i in range(homework):
    while True:
        # گرفتن نمره هر Homework
        mark_homework = float(input(Fore.YELLOW + "What is your mark for homework (0-100): "))
        if mark_homework < 0 or mark_homework > 100:
            # بررسی معتبر بودن نمره
            print(Fore.RED + "Your score must be between 0 and 100.")
        else:
            # اضافه کردن نمره به جمع
            test_homework += mark_homework
            break

# محاسبه میانگین Homework
average = test_homework / homework
print(Fore.GREEN + "For homework your score is:", average, "%")

# ------------------------------
# بخش Exam
# ------------------------------
Exam = int(input(Fore.CYAN + "How many exams do you have? "))
test_Exam = 0  # جمع نمره‌های Exam

for i in range(Exam):
    while True:
        # گرفتن نمره هر Exam
        mark_Exam = float(input(Fore.YELLOW + "What is your mark for Exam (0-100): "))
        if mark_Exam < 0 or mark_Exam > 100:
            # بررسی معتبر بودن نمره
            print(Fore.RED + "Your score must be between 0 and 100.")
        else:
            # اضافه کردن نمره به جمع
            test_Exam += mark_Exam
            break

# محاسبه میانگین Exam
average_Exam = test_Exam / Exam
print(Fore.GREEN + "For Exam your score is:", average_Exam, "%")

# ------------------------------
# بخش CPT
# ------------------------------
cpt_count = int(input(Fore.CYAN + "How many CPTs did you have? "))
total_cpt = 0  # جمع نمره‌های CPT

for i in range(cpt_count):
    while True:
        # گرفتن نمره هر CPT
        mark = float(input(Fore.YELLOW + "What is your mark for CPT (0-100): "))
        if mark < 0 or mark > 100:
            print(Fore.RED + "Score must be between 0 and 100.")
        else:
            total_cpt += mark
            break

# محاسبه میانگین CPT
average_cpt = total_cpt / cpt_count
print(Fore.GREEN + "CPT average:", average_cpt, "%")

# ------------------------------
# محاسبه نمره نهایی ساده
# ------------------------------
# میانگین ساده Homework + Exam + CPT
final_score = (average + average_Exam + average_cpt) / 3
print(Fore.MAGENTA + Style.BRIGHT + "Your FINAL SCORE is:", final_score, "%")

# ------------------------------
# محاسبه نمره نهایی وزنی
# ------------------------------
weight_homework = 0.2  # Homework 20%
weight_exam = 0.6      # Exam 60%
weight_cpt = 0.2       # CPT 20%

# نمره نهایی وزنی = میانگین هر بخش * وزنش
final_weighted_score = (average * weight_homework +
                        average_Exam * weight_exam +
                        average_cpt * weight_cpt)
print(Fore.MAGENTA + Style.BRIGHT + f"Your FINAL WEIGHTED SCORE is: {final_weighted_score:.2f}%")
