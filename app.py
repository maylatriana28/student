import os
import joblib
import pandas as pd
import streamlit as st


# =========================================================
# KONFIGURASI HALAMAN
# =========================================================
st.set_page_config(
    page_title="Prediksi Status Mahasiswa",
    page_icon="🎓",
    layout="wide"
)


# =========================================================
# LOAD MODEL
# =========================================================
MODEL_PATH = os.path.join(
    "model",
    "student_status_model.pkl"
)


@st.cache_resource
def load_model():
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(
            f"Model tidak ditemukan pada: {MODEL_PATH}"
        )

    return joblib.load(MODEL_PATH)


try:
    model = load_model()

except Exception as e:
    st.error(
        "Model gagal dimuat. "
        "Pastikan file student_status_model.pkl "
        "tersedia di dalam folder model."
    )

    st.exception(e)
    st.stop()


# =========================================================
# JUDUL APLIKASI
# =========================================================
st.title("🎓 Prediksi Status Akhir Mahasiswa")

st.write(
    """
    Aplikasi ini digunakan untuk memperkirakan status akhir mahasiswa
    berdasarkan karakteristik akademik, demografi, dan kondisi lainnya.

    Model akan menghasilkan salah satu dari dua prediksi:

    - **Dropout**
    - **Graduate**

    Hasil prediksi dapat digunakan sebagai alat bantu untuk
    mengidentifikasi mahasiswa yang berpotensi mengalami dropout
    sehingga institusi dapat melakukan monitoring atau intervensi
    lebih awal.
    """
)

st.info(
    "Hasil prediksi merupakan alat bantu analisis dan bukan keputusan "
    "mutlak mengenai status akhir mahasiswa."
)

st.divider()


# =========================================================
# FORM INPUT
# =========================================================
with st.form("prediction_form"):

    # =====================================================
    # 1. INFORMASI UMUM
    # =====================================================
    st.subheader("1. Informasi Umum Mahasiswa")

    col1, col2, col3 = st.columns(3)

    with col1:
        Marital_status = st.number_input(
            "Marital Status",
            min_value=1,
            value=1,
            step=1
        )

        Application_mode = st.number_input(
            "Application Mode",
            min_value=1,
            value=1,
            step=1
        )

        Application_order = st.number_input(
            "Application Order",
            min_value=0,
            value=1,
            step=1
        )

        Course = st.number_input(
            "Course",
            min_value=1,
            value=9238,
            step=1
        )

    with col2:
        Daytime_evening_attendance = st.selectbox(
            "Daytime / Evening Attendance",
            options=[1, 0],
            format_func=lambda x: (
                "Daytime"
                if x == 1
                else "Evening"
            )
        )

        Previous_qualification = st.number_input(
            "Previous Qualification",
            min_value=1,
            value=1,
            step=1
        )

        Previous_qualification_grade = st.number_input(
            "Previous Qualification Grade",
            min_value=0.0,
            max_value=200.0,
            value=120.0,
            step=1.0
        )

        Nacionality = st.number_input(
            "Nationality",
            min_value=1,
            value=1,
            step=1
        )

    with col3:
        Admission_grade = st.number_input(
            "Admission Grade",
            min_value=0.0,
            max_value=200.0,
            value=120.0,
            step=1.0
        )

        Gender = st.selectbox(
            "Gender",
            options=[0, 1],
            format_func=lambda x: (
                "Female"
                if x == 0
                else "Male"
            )
        )

        Age_at_enrollment = st.number_input(
            "Age at Enrollment",
            min_value=15,
            max_value=100,
            value=20,
            step=1
        )

        International = st.selectbox(
            "International Student",
            options=[0, 1],
            format_func=lambda x: (
                "No"
                if x == 0
                else "Yes"
            )
        )


    # =====================================================
    # 2. LATAR BELAKANG KELUARGA
    # =====================================================
    st.subheader("2. Latar Belakang Keluarga")

    col1, col2 = st.columns(2)

    with col1:
        Mothers_qualification = st.number_input(
            "Mother's Qualification",
            min_value=1,
            value=1,
            step=1
        )

        Mothers_occupation = st.number_input(
            "Mother's Occupation",
            min_value=0,
            value=0,
            step=1
        )

    with col2:
        Fathers_qualification = st.number_input(
            "Father's Qualification",
            min_value=1,
            value=1,
            step=1
        )

        Fathers_occupation = st.number_input(
            "Father's Occupation",
            min_value=0,
            value=0,
            step=1
        )


    # =====================================================
    # 3. KONDISI SOSIAL DAN FINANSIAL
    # =====================================================
    st.subheader("3. Kondisi Sosial dan Finansial")

    col1, col2, col3 = st.columns(3)

    with col1:
        Displaced = st.selectbox(
            "Displaced",
            options=[0, 1],
            format_func=lambda x: (
                "No"
                if x == 0
                else "Yes"
            )
        )

        Educational_special_needs = st.selectbox(
            "Educational Special Needs",
            options=[0, 1],
            format_func=lambda x: (
                "No"
                if x == 0
                else "Yes"
            )
        )

    with col2:
        Debtor = st.selectbox(
            "Debtor",
            options=[0, 1],
            format_func=lambda x: (
                "No"
                if x == 0
                else "Yes"
            )
        )

        Tuition_fees_up_to_date = st.selectbox(
            "Tuition Fees Up To Date",
            options=[0, 1],
            format_func=lambda x: (
                "No"
                if x == 0
                else "Yes"
            )
        )

    with col3:
        Scholarship_holder = st.selectbox(
            "Scholarship Holder",
            options=[0, 1],
            format_func=lambda x: (
                "No"
                if x == 0
                else "Yes"
            )
        )


    # =====================================================
    # 4. PERFORMA AKADEMIK SEMESTER 1
    # =====================================================
    st.subheader("4. Performa Akademik Semester 1")

    col1, col2, col3 = st.columns(3)

    with col1:
        Curricular_units_1st_sem_credited = st.number_input(
            "1st Semester - Credited",
            min_value=0,
            value=0,
            step=1
        )

        Curricular_units_1st_sem_enrolled = st.number_input(
            "1st Semester - Enrolled",
            min_value=0,
            value=6,
            step=1
        )

    with col2:
        Curricular_units_1st_sem_evaluations = st.number_input(
            "1st Semester - Evaluations",
            min_value=0,
            value=6,
            step=1
        )

        Curricular_units_1st_sem_approved = st.number_input(
            "1st Semester - Approved",
            min_value=0,
            value=5,
            step=1
        )

    with col3:
        Curricular_units_1st_sem_grade = st.number_input(
            "1st Semester - Grade",
            min_value=0.0,
            max_value=20.0,
            value=12.0,
            step=0.1
        )

        Curricular_units_1st_sem_without_evaluations = (
            st.number_input(
                "1st Semester - Without Evaluations",
                min_value=0,
                value=0,
                step=1
            )
        )


    # =====================================================
    # 5. PERFORMA AKADEMIK SEMESTER 2
    # =====================================================
    st.subheader("5. Performa Akademik Semester 2")

    col1, col2, col3 = st.columns(3)

    with col1:
        Curricular_units_2nd_sem_credited = st.number_input(
            "2nd Semester - Credited",
            min_value=0,
            value=0,
            step=1
        )

        Curricular_units_2nd_sem_enrolled = st.number_input(
            "2nd Semester - Enrolled",
            min_value=0,
            value=6,
            step=1
        )

    with col2:
        Curricular_units_2nd_sem_evaluations = st.number_input(
            "2nd Semester - Evaluations",
            min_value=0,
            value=6,
            step=1
        )

        Curricular_units_2nd_sem_approved = st.number_input(
            "2nd Semester - Approved",
            min_value=0,
            value=5,
            step=1
        )

    with col3:
        Curricular_units_2nd_sem_grade = st.number_input(
            "2nd Semester - Grade",
            min_value=0.0,
            max_value=20.0,
            value=12.0,
            step=0.1
        )

        Curricular_units_2nd_sem_without_evaluations = (
            st.number_input(
                "2nd Semester - Without Evaluations",
                min_value=0,
                value=0,
                step=1
            )
        )


    # =====================================================
    # 6. KONDISI EKONOMI
    # =====================================================
    st.subheader("6. Kondisi Ekonomi")

    col1, col2, col3 = st.columns(3)

    with col1:
        Unemployment_rate = st.number_input(
            "Unemployment Rate",
            value=10.0,
            step=0.1
        )

    with col2:
        Inflation_rate = st.number_input(
            "Inflation Rate",
            value=1.0,
            step=0.1
        )

    with col3:
        GDP = st.number_input(
            "GDP",
            value=0.0,
            step=0.1
        )


    # =====================================================
    # TOMBOL PREDIKSI
    # =====================================================
    submitted = st.form_submit_button(
        "Prediksi Status Mahasiswa",
        use_container_width=True
    )


# =========================================================
# PROSES PREDIKSI
# =========================================================
if submitted:

    input_data = pd.DataFrame(
        [{
            "Marital_status":
                Marital_status,

            "Application_mode":
                Application_mode,

            "Application_order":
                Application_order,

            "Course":
                Course,

            "Daytime_evening_attendance":
                Daytime_evening_attendance,

            "Previous_qualification":
                Previous_qualification,

            "Previous_qualification_grade":
                Previous_qualification_grade,

            "Nacionality":
                Nacionality,

            "Mothers_qualification":
                Mothers_qualification,

            "Fathers_qualification":
                Fathers_qualification,

            "Mothers_occupation":
                Mothers_occupation,

            "Fathers_occupation":
                Fathers_occupation,

            "Admission_grade":
                Admission_grade,

            "Displaced":
                Displaced,

            "Educational_special_needs":
                Educational_special_needs,

            "Debtor":
                Debtor,

            "Tuition_fees_up_to_date":
                Tuition_fees_up_to_date,

            "Gender":
                Gender,

            "Scholarship_holder":
                Scholarship_holder,

            "Age_at_enrollment":
                Age_at_enrollment,

            "International":
                International,

            "Curricular_units_1st_sem_credited":
                Curricular_units_1st_sem_credited,

            "Curricular_units_1st_sem_enrolled":
                Curricular_units_1st_sem_enrolled,

            "Curricular_units_1st_sem_evaluations":
                Curricular_units_1st_sem_evaluations,

            "Curricular_units_1st_sem_approved":
                Curricular_units_1st_sem_approved,

            "Curricular_units_1st_sem_grade":
                Curricular_units_1st_sem_grade,

            "Curricular_units_1st_sem_without_evaluations":
                Curricular_units_1st_sem_without_evaluations,

            "Curricular_units_2nd_sem_credited":
                Curricular_units_2nd_sem_credited,

            "Curricular_units_2nd_sem_enrolled":
                Curricular_units_2nd_sem_enrolled,

            "Curricular_units_2nd_sem_evaluations":
                Curricular_units_2nd_sem_evaluations,

            "Curricular_units_2nd_sem_approved":
                Curricular_units_2nd_sem_approved,

            "Curricular_units_2nd_sem_grade":
                Curricular_units_2nd_sem_grade,

            "Curricular_units_2nd_sem_without_evaluations":
                Curricular_units_2nd_sem_without_evaluations,

            "Unemployment_rate":
                Unemployment_rate,

            "Inflation_rate":
                Inflation_rate,

            "GDP":
                GDP
        }]
    )

    try:

        # Prediksi kelas
        prediction = model.predict(
            input_data
        )[0]

        # Probabilitas
        probabilities = model.predict_proba(
            input_data
        )[0]

        # Ambil nama kelas dari classifier pipeline
        classifier = model.named_steps[
            "classifier"
        ]

        classes = list(
            classifier.classes_
        )

        dropout_index = classes.index(
            "Dropout"
        )

        graduate_index = classes.index(
            "Graduate"
        )

        dropout_probability = probabilities[
            dropout_index
        ]

        graduate_probability = probabilities[
            graduate_index
        ]

        st.divider()

        st.subheader("Hasil Prediksi")

        # =================================================
        # HASIL DROPOUT
        # =================================================
        if prediction == "Dropout":

            st.error(
                "⚠️ Mahasiswa diprediksi berpotensi "
                "mengalami DROPOUT."
            )

            st.write(
                """
                Hasil ini menunjukkan bahwa berdasarkan pola
                yang dipelajari model dari data historis,
                mahasiswa memiliki karakteristik yang lebih
                dekat dengan kelompok mahasiswa yang mengalami
                dropout.

                Mahasiswa dengan hasil prediksi ini dapat
                diprioritaskan untuk monitoring dan evaluasi
                lebih lanjut oleh pihak institusi.
                """
            )

        # =================================================
        # HASIL GRADUATE
        # =================================================
        else:

            st.success(
                "✅ Mahasiswa diprediksi berpotensi "
                "GRADUATE."
            )

            st.write(
                """
                Berdasarkan karakteristik yang dimasukkan,
                mahasiswa memiliki pola yang lebih dekat
                dengan kelompok mahasiswa yang berhasil
                menyelesaikan pendidikan.
                """
            )


        # =================================================
        # PROBABILITAS
        # =================================================
        st.subheader(
            "Probabilitas Prediksi"
        )

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                label="Probabilitas Dropout",
                value=(
                    f"{dropout_probability:.2%}"
                )
            )

        with col2:

            st.metric(
                label="Probabilitas Graduate",
                value=(
                    f"{graduate_probability:.2%}"
                )
            )


        # Progress probabilitas dropout
        st.write(
            "**Tingkat probabilitas Dropout**"
        )

        st.progress(
            float(dropout_probability)
        )


        # =================================================
        # KATEGORI RISIKO
        # =================================================
        if dropout_probability >= 0.70:

            risk_level = "Tinggi"

            st.error(
                "Tingkat risiko dropout: TINGGI"
            )

        elif dropout_probability >= 0.40:

            risk_level = "Sedang"

            st.warning(
                "Tingkat risiko dropout: SEDANG"
            )

        else:

            risk_level = "Rendah"

            st.success(
                "Tingkat risiko dropout: RENDAH"
            )


        # =================================================
        # REKOMENDASI
        # =================================================
        if risk_level == "Tinggi":

            st.subheader(
                "Rekomendasi Tindak Lanjut"
            )

            st.write(
                """
                Mahasiswa dapat diprioritaskan untuk evaluasi
                lebih lanjut, seperti:

                - Konsultasi dengan dosen pembimbing akademik.
                - Evaluasi performa akademik.
                - Pemeriksaan kendala pembayaran biaya pendidikan.
                - Evaluasi kebutuhan bantuan finansial.
                - Pendampingan atau program dukungan belajar.
                """
            )

        elif risk_level == "Sedang":

            st.subheader(
                "Rekomendasi Tindak Lanjut"
            )

            st.write(
                """
                Mahasiswa dapat dimasukkan ke dalam monitoring
                berkala untuk melihat perkembangan akademik
                dan kondisi lainnya yang dapat memengaruhi
                keberlanjutan studi.
                """
            )

        else:

            st.write(
                """
                Risiko dropout berdasarkan model relatif rendah.
                Monitoring akademik secara berkala tetap
                disarankan.
                """
            )


    except Exception as e:

        st.error(
            "Terjadi kesalahan saat melakukan prediksi."
        )

        st.exception(e)


# =========================================================
# INFORMASI MODEL
# =========================================================
st.divider()

with st.expander(
    "Tentang Sistem Prediksi"
):

    st.write(
        """
        Sistem prediksi ini dibangun menggunakan model
        machine learning yang dilatih menggunakan data
        mahasiswa dengan status akhir **Dropout** dan
        **Graduate**.

        Mahasiswa dengan status **Enrolled tidak digunakan
        sebagai data training**, karena mahasiswa tersebut
        belum memiliki status akhir.

        Model dapat digunakan sebagai alat bantu untuk
        memperkirakan kemungkinan status akhir mahasiswa
        aktif menjadi Dropout atau Graduate berdasarkan
        karakteristik yang dimasukkan.

        Hasil prediksi tidak dimaksudkan sebagai keputusan
        otomatis mengenai mahasiswa. Hasil model sebaiknya
        digunakan bersama evaluasi akademik dan pertimbangan
        pihak institusi.
        """
    )