from sklearn import svm

def get_playbook():
    return svm.LinearSVC()

def train(svc, train_in, train_out):
    return svc.fit(train_in, train_out)
