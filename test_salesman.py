import salesman

def test_smalldataset():
    route, distance = salesman.salesman('swedendataset.csv')
    assert distance == 916.0


def test_smalldataset():
    route, distance = salesman.salesman('eurotripdataset.csv')
    assert distance == 9826.0
    
