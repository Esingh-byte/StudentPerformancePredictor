import streamlit as st
import pickle
import numpy as np
import plotly.graph_objects as go
import time

# --- Page configuration ---
st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- Custom CSS for styling ---
st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600;700&display=swap');

    /* Main Background Gradient */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Poppins', sans-serif;
    }

    /* Sidebar Styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #667eea 0%, #764ba2 100%);
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }

    /* Card/Block styling */
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.3);
        backdrop-filter: blur(10px);
    }

    /* Headers */
    h1 {
        color: white !important;
        font-weight: 700 !important;
        text-align: center;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.3);
        font-size: 3.5em !important;
        margin-bottom: 10px !important;
        animation: fadeInDown 0.8s ease;
    }

    h2, h3 {
        color: #667eea !important;
        font-weight: 600 !important;
        border-bottom: 3px solid #667eea;
        padding-bottom: 10px;
        margin-top: 20px !important;
    }

    h4 {
        color: #764ba2 !important;
        font-weight: 600 !important;
    }

    /* Input fields */
    .stNumberInput > div > div > input,
    .stSelectbox > div > div > select,
    .stSlider > div > div > div {
        border: 2px solid #e0e0e0 !important;
        border-radius: 10px !important;
        font-size: 1.1em !important;
        transition: all 0.3s ease !important;
    }

    .stNumberInput > div > div > input:focus,
    .stSelectbox > div > div > select:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2) !important;
    }

    /* Labels */
    .stNumberInput > label,
    .stSelectbox > label,
    .stSlider > label {
        font-weight: 600 !important;
        font-size: 1.1em !important;
        color: #333 !important;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 20px !important;
        font-size: 1.4em !important;
        font-weight: 700 !important;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 8px 20px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s ease !important;
        margin-top: 30px !important;
    }

    .stButton > button:hover {
        transform: translateY(-3px) !important;
        box-shadow: 0 12px 30px rgba(102, 126, 234, 0.6) !important;
    }

    .stButton > button:active {
        transform: translateY(-1px) !important;
    }

    /* Metrics */
    [data-testid="stMetricValue"] {
        font-size: 1.8em !important;
        font-weight: 700 !important;
        color: #667eea !important;
    }

    [data-testid="stMetricLabel"] {
        font-weight: 600 !important;
        color: #666 !important;
    }

    /* Info/Success/Warning boxes */
    .stAlert {
        border-radius: 15px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1) !important;
        font-weight: 500 !important;
    }

    /* Progress bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%) !important;
        border-radius: 10px !important;
        height: 20px !important;
    }

    /* Animations */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes fadeIn {
        from {
            opacity: 0;
            transform: translateY(20px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    @keyframes pulse {
        0%, 100% {
            transform: scale(1);
        }
        50% {
            transform: scale(1.05);
        }
    }

    /* Prediction box custom styling */
    .prediction-box-pass {
        background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
        color: #155724;
        border: 3px solid #28a745;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        font-size: 2em;
        font-weight: 700;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(40, 167, 69, 0.3);
        animation: pulse 2s infinite;
    }

    .prediction-box-fail {
        background: linear-gradient(135deg, #f8d7da 0%, #f5c6cb 100%);
        color: #721c24;
        border: 3px solid #dc3545;
        border-radius: 20px;
        padding: 40px;
        text-align: center;
        font-size: 2em;
        font-weight: 700;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(220, 53, 69, 0.3);
        animation: pulse 2s infinite;
    }

    .grade-display {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 25px;
        padding: 50px;
        text-align: center;
        margin: 30px 0;
        box-shadow: 0 15px 50px rgba(102, 126, 234, 0.5);
        animation: fadeIn 0.8s ease;
    }

    .grade-number {
        font-size: 6em;
        font-weight: 900;
        margin: 20px 0;
        text-shadow: 3px 3px 10px rgba(0,0,0,0.3);
        animation: pulse 2s infinite;
    }

    /* Subtitle styling */
    .subtitle {
        color: white !important;
        text-align: center;
        font-size: 1.3em !important;
        margin-bottom: 30px !important;
        text-shadow: 1px 1px 4px rgba(0,0,0,0.2);
        animation: fadeInDown 1s ease;
    }

    /* Badge */
    .badge {
        display: inline-block;
        background: rgba(255,255,255,0.25);
        padding: 8px 20px;
        border-radius: 25px;
        font-size: 0.9em;
        color: white;
        margin-top: 10px;
        font-weight: 600;
        backdrop-filter: blur(10px);
        animation: fadeIn 1.2s ease;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}

    /* Metric cards styling */
    [data-testid="stMetricValue"] > div {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 15px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# --- Load model ---
@st.cache_resource
def load_model():
    """Loads the pickled model file."""
    try:
        # Changed filename to match your notebook save
        with open('studentgrade.pkl', 'rb') as file:
            model = pickle.load(file)
        return model, True
    except FileNotFoundError:
        return None, False

model, model_loaded = load_model()

# --- Header with animation ---
st.markdown('<h1>🎓 Student Performance Predictor</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Predict your final grade using AI-powered machine learning</p>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# --- Check if model is loaded ---
if not model_loaded:
    # Updated filename in error message
    st.error("⚠️ **Error:** `studentgrades.pkl` file not found! Please ensure it's in the same directory as this script.")
    st.stop()


# --- Main content ---
col1, col2 = st.columns([1.2, 1], gap="large")

with col1:
    st.markdown("###  Enter Your Academic Information")

    # Grade inputs
    st.markdown("####  Period Grades")
    grade_col1, grade_col2 = st.columns(2)

    with grade_col1:
        g1 = st.number_input(
            "First Period Grade (G1)",
            min_value=0.0,
            max_value=20.0,
            value=14.0,  # Default value
            step=0.5,
            help="Your grade from the first grading period (0-20 scale)"
        )

    with grade_col2:
        g2 = st.number_input(
            "Second Period Grade (G2)",
            min_value=0.0,
            max_value=20.0,
            value=16.0,  # Default value
            step=0.5,
            help="Your grade from the second grading period (0-20 scale)"
        )

    st.markdown("####  Study Habits & Lifestyle")

    study_col1, study_col2 = st.columns(2)

    with study_col1:
        studytime = st.selectbox(
            "Weekly Study Time",
            options=[1, 2, 3, 4],
            index=1,  # Default index (corresponds to '2-5 hours/week')
            format_func=lambda x: {
                1: "1 hour",
                2: "2 hour",
                3: "3 hour",
                4: "4 hour"
            }.get(x, "Unknown") # Added .get for safety
        )

        health = st.selectbox(
            "Current Health Status",
            options=[1, 2, 3, 4, 5],
            index=2,  # Default index (corresponds to 'Average')
            format_func=lambda x: {
                1: "Very Bad",
                2: "Bad",
                3: "Average",
                4: "Good",
                5: "Very Good"
            }.get(x, "Unknown")
        )

    with study_col2:
        famrel = st.selectbox(
            "Family Relationships Quality",
            options=[1, 2, 3, 4, 5],
            index=4,  # Default index (corresponds to 'Very Good')
            format_func=lambda x: {
                1: "Very Bad",
                2: "Bad",
                3: "Average",
                4: "Good",
                5: "Very Good"
            }.get(x, "Unknown")
        )

        failures = st.number_input(
            "Past Class Failures",
            min_value=0,
            max_value=4, # Max based on dataset description
            value=0,   # Default value
            help="Number of times you've failed a class (0-4)"
        )

    st.markdown("####  Attendance Record")

    absences = st.slider(
        "Total School Absences",
        min_value=0,
        max_value=93, # Max based on dataset description
        value=5,    # Default value
        help="Total number of days absent from school (0-93)"
    )

    # Predict button
    predict_button = st.button("🔮 PREDICT MY FINAL GRADE", use_container_width=True)

with col2:
    st.markdown("###  Prediction Results")

    if predict_button:
        # Add a brief loading animation
        with st.spinner(' Analyzing your data with AI...'):
            time.sleep(1)  # Dramatic effect!

        # Prepare data and predict
        # Ensure the order matches the features used in training!
        # G1, G2, studytime, health, famrel, failures, absences
        user_data = np.array([[g1, g2, studytime, health, famrel, failures, absences]])
        predicted_score = model.predict(user_data)[0]

        # Clip the predicted score to be within the valid range (0-20)
        predicted_score = float(np.clip(predicted_score, 0, 20))

        # Display grade in a styled box
        st.markdown(f"""
        <div class="grade-display">
            <h3 style="color: white; opacity: 0.9; font-size: 1.3em; margin: 0;">Predicted Final Grade (G3)</h3>
            <div class="grade-number">{predicted_score:.1f}</div>
            <p style="color: white; opacity: 0.9; font-size: 1.2em; margin: 0;">out of 20</p>
        </div>
        """, unsafe_allow_html=True)

        # Pass/Fail status with animation
        if predicted_score >= 10:
            st.markdown("""
                <div class="prediction-box-pass">
                    ✅ YOU WILL PASS! 🎉
                </div>
            """, unsafe_allow_html=True)
            st.balloons()  # Celebration!
        else:
            st.markdown("""
                <div class="prediction-box-fail">
                    ⚠️ AT RISK OF FAILING
                </div>
            """, unsafe_allow_html=True)
            st.warning("💪 Don't worry! You can improve with the right strategies.")

        # Progress indicator
        st.markdown("#### 📈 Grade Achievement")
        progress = predicted_score / 20.0
        st.progress(progress)
        st.markdown(f"**{progress*100:.1f}%** of maximum grade achieved")

        # Performance metrics
        st.markdown("#### 📉 Performance Metrics")
        metric_col1, metric_col2, metric_col3 = st.columns(3)

        with metric_col1:
            trend = g2 - g1
            trend_emoji = "📈" if trend > 0 else "📉" if trend < 0 else "➡️"
            st.metric("Grade Trend (G2-G1)", f"{trend_emoji} {abs(trend):.1f}", delta=f"{trend:+.1f} pts")

        with metric_col2:
            study_score = "Excellent" if studytime >= 3 else "Good" if studytime == 2 else "Low"
            study_emoji = "🔥" if studytime >= 3 else "👍" if studytime == 2 else "⚠️"
            st.metric("Study Habits", f"{study_emoji} {study_score}")

        with metric_col3:
            # Assuming max absences is 93 for percentage calculation
            attendance_percent = max(0, ((93 - absences) / 93.0)) * 100
            st.metric("Attendance", f"{attendance_percent:.0f}%")

        # Grade comparison chart
        st.markdown("#### 📊 Grade Progression Chart")

        fig = go.Figure()

        grades = ['G1<br>First Period', 'G2<br>Second Period', 'G3<br>Predicted']
        values = [g1, g2, predicted_score]
        colors = ['#FF6B6B', '#4ECDC4', '#667eea'] # Different colors for bars

        fig.add_trace(go.Bar(
            x=grades,
            y=values,
            marker=dict(
                color=colors,
                line=dict(color='white', width=2)
            ),
            text=[f'<b>{v:.1f}</b>' for v in values],
            textposition='outside',
            textfont=dict(size=18, color='black', family='Poppins'),
            hovertemplate='<b>%{x}</b><br>Grade: %{y:.1f}/20<extra></extra>'
        ))

        fig.update_layout(
            yaxis_range=[0, 22], # Range slightly above max grade
            yaxis_title="<b>Grade (out of 20)</b>",
            height=400,
            showlegend=False,
            plot_bgcolor='rgba(255,255,255,0.9)',
            paper_bgcolor='rgba(0,0,0,0)', # Transparent background
            font=dict(family='Poppins', size=14),
            yaxis=dict(gridcolor='rgba(0,0,0,0.1)')
        )

        st.plotly_chart(fig, use_container_width=True)

        # Smart suggestions (only if predicted score suggests improvement needed)
        if predicted_score < 15: # Threshold for showing suggestions
            st.markdown("#### 💡 Personalized Improvement Strategies")

            suggestions = []
            if studytime < 3:
                suggestions.append("📚 **Increase Study Time**: Aim for at least 5-10 hours per week for better retention.")
            if absences > 10: # Suggest if absences are relatively high
                suggestions.append("🏫 **Improve Attendance**: Missing class significantly impacts learning. Try to attend regularly!")
            if failures > 0:
                suggestions.append("💪 **Overcome Past Failures**: Consider tutoring or extra help in challenging subjects.")
            if health < 4:
                suggestions.append("🏃 **Prioritize Health**: Good sleep, nutrition, and exercise boost academic performance!")
            if famrel < 4:
                suggestions.append("❤️ **Seek Support**: Talk to family, teachers, or counselors for guidance.")
            if g2 < g1:
                suggestions.append("📉 **Reverse the Trend**: Your grades seem to be declining. Identify problem areas and seek help early!")

            if suggestions:
                for i, suggestion in enumerate(suggestions, 1):
                    st.info(f"**{i}.** {suggestion}")
            elif predicted_score >= 10: # If score is >= 10 but < 15 and no specific suggestions
                 st.success("✨ **Good job passing!** Keep refining your study habits to aim even higher!")

    else:
        st.info("👈 Fill in your academic information on the left and click the **PREDICT** button to see your personalized results!")
        # Placeholder image or info when no prediction has been made
        st.image("https://img.icons8.com/clouds/400/000000/test-passed.png", use_column_width=True)

# --- Footer ---
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: white; padding: 30px; font-size: 0.9em;'>
        <p style='font-weight: 600; font-size: 1.1em;'>🎓 Student Performance Predictor</p>
        <p>Built with ❤️ using Streamlit & Machine Learning</p>
        <p style='font-size: 0.85em; opacity: 0.8;'>⚠️ Predictions are based on historical data patterns and should be used as guidance only.</p>
    </div>
""", unsafe_allow_html=True)