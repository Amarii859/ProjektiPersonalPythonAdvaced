import streamlit as st
from crud import add_student, get_students, delete_student, update_student

st.set_page_config(page_title="School System", page_icon="📚", layout="wide")

st.title("📚 School Management System")

menu = st.sidebar.selectbox(
    "Navigation",
    ["🏠 Home", "➕ Add Student", "📋 View Students", "✏️ Edit Student", "🗑️ Delete Student"]
)

# ---------------- HOME ----------------
if menu == "🏠 Home":
    students = get_students()
    total_students = len(students)

    st.markdown("## 👋 Welcome to School Management System")
    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <div style="padding:20px;border-radius:10px;background:#262730;text-align:center;">
                <h2>📚</h2>
                <h3>{total_students}</h3>
                <p>Total Students</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div style="padding:20px;border-radius:10px;background:#262730;text-align:center;">
                <h2>🏫</h2>
                <h3>School</h3>
                <p>System Status</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div style="padding:20px;border-radius:10px;background:#262730;text-align:center;">
                <h2>⚡</h2>
                <h3>Active</h3>
                <p>Database Status</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    st.subheader("📌 Recent Students")

    if students:
        for s in students[-5:]:
            st.write(f"👤 {s[1]} {s[2]} | 📘 {s[3]} | 🎂 {s[4]}")
    else:
        st.info("No students added yet.")

    st.markdown("---")

    st.markdown("""
    ### 🚀 Quick Tips
    - ➕ Add students easily  
    - 📋 View full list  
    - ✏️ Edit existing students  
    - 🗑️ Delete unwanted records  
    """)

# ---------------- ADD ----------------
elif menu == "➕ Add Student":
    st.subheader("➕ Add New Student")

    with st.form("add_form", clear_on_submit=True):
        name = st.text_input("Name")
        surname = st.text_input("Surname")
        class_name = st.text_input("Class")
        age = st.number_input("Age", min_value=1, step=1)

        submitted = st.form_submit_button("Add Student")

        if submitted:
            if name and surname and class_name:
                add_student(name, surname, class_name, int(age))
                st.success("Student added successfully!")
            else:
                st.error("Please fill all fields!")

# ---------------- VIEW ----------------
elif menu == "📋 View Students":
    st.subheader("📋 Students List")

    students = get_students()

    if students:
        for s in students:
            st.markdown(
                f"""
                <div style="
                    padding:15px;
                    border-radius:10px;
                    margin-bottom:10px;
                    background-color:#1f1f1f;
                    border:1px solid #333;">
                    <h4>👤 {s[1]} {s[2]}</h4>
                    <p>📘 Class: {s[3]}</p>
                    <p>🎂 Age: {s[4]}</p>
                    <p><b>ID:</b> {s[0]}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info("No students found.")

# ---------------- EDIT ----------------
elif menu == "✏️ Edit Student":
    st.subheader("✏️ Update Student")

    student_id = st.number_input("Student ID", min_value=1, step=1)

    name = st.text_input("New Name")
    surname = st.text_input("New Surname")
    class_name = st.text_input("New Class")
    age = st.number_input("New Age", min_value=1, step=1)

    if st.button("Update"):
        update_student(student_id, name, surname, class_name, int(age))
        st.success("Student updated successfully!")

# ---------------- DELETE ----------------
elif menu == "🗑️ Delete Student":
    st.subheader("🗑️ Delete Student")

    student_id = st.number_input("Student ID", min_value=1, step=1)

    if st.button("Delete"):
        delete_student(student_id)
        st.success("Student deleted successfully!")