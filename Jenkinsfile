pipeline {
    agent {
        docker { image 'python:3.8' }
    }
    
    stages {
        stage('Deploy') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'streamlit run app.py --server.address=0.0.0.0 --server.port=8501 &'
            }
        }
    }
}


