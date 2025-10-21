# Danh sách để lưu các công việc
task = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách."""
    tasks.append(task_name)
    print(f"Đã thêm công việc: '{task_name}'")
# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
    print("Chào mừng đến với ứng dụng To-Do List!")
    add_task("Học bài Git và GitHub")
    add_task("Làm bài tập thực hành ở nhà")

##BTVN
#Liet ke tat ca cong viec
tasks = []
def add_task(name):
    tasks.append(name)
    print(f"Đã thêm công việc: {name}")
def list_tasks():
    if not tasks:
        print("Không có công việc nào.")
    else:
        print("Danh sách công việc:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")
if __name__ == "__main__":
    add_task("Học bài Git")
    add_task("Làm bài tập")
    list_tasks()


## Thay đổi ds task
def complete_task(index):
    if 0 <= index < len(tasks):
        tasks[index] += " ✅ (Hoàn thành)"
        print(f"Đã đánh dấu hoàn thành: {tasks[index]}")
    else:
        print("Không tìm thấy công việc này.")
if __name__ == "__main__":
    add_task("Học Git")
    add_task("Làm bài tập")
    complete_task(0)
    list_tasks()

#Xoá một công việc
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f"🗑️ Đã xóa công việc: {deleted_task['name']}")
    else:
        print("❌ Chỉ số không hợp lệ.")

if __name__ == "__main__":
    add_task("Học Git")
    add_task("Làm bài Python")
    list_tasks()
    print("\n--- Sau khi xóa ---")
    delete_task(0)
    list_tasks()
