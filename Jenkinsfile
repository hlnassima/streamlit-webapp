pipeline {
    agent any
    
    stages {
        stage('Deploy') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                    sh 'streamlit run app.py --server.address=0.0.0.0 --server.port=8501 &'
                }
            }
        }
    }
}


