pipeline {
    agent any
    
    stages {
        stage('Deploy') {
            steps {
                script {
                    env.PATH = "/var/lib/jenkins/.local/bin:${env.PATH}"
                    sh 'pip install -r requirements.txt'
                    sh 'streamlit run app.py --server.address=0.0.0.1 --server.port=8501 &'
                }
            }
        }
    }
}


