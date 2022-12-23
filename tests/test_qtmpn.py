from mpn_lookup import QTArrays


def test_qt51():
    # 18 22.2 14.1 35.2
    assert QTArrays.getQTmpn(18) == [22.2,14.1,35.2]
    # 0 <1.0 0.0 3.7
    assert QTArrays.getQTmpn(0) == ['<1.0',0.0,3.7]
    # 51 > 200.5 146.1 infinite
    assert QTArrays.getQTmpn(51) == ['>200.5',146.1,'infinite']
    # 30 45.3 31.5 65.6
    assert QTArrays.getQTmpn(30) == [45.3,31.5,65.6]

    # bad input
    assert QTArrays.getQTmpn(-1) is None
    assert QTArrays.getQTmpn('b') is None
    assert QTArrays.getQTmpn(52) is None


def test_qt2k():
    # [59.3, 44.6, 77.2]
    assert QTArrays.getQT2Kmpn(22, 22) == [59.3, 44.6, 77.2]
    # ['&lt;1', 0.0, 3.7]
    assert QTArrays.getQT2Kmpn(0, 0) == ['<1', 0.0, 3.7]
    # ['&gt;2419.6', 1439.5, 'infinite']
    assert QTArrays.getQT2Kmpn(49, 48) == ['>2419.6', 1439.5, 'infinite']

    # bad input
    assert QTArrays.getQT2Kmpn(-2, -10) is None

    assert QTArrays.getQT2Kmpn('q','a') is None


def test_legio():
    assert QTArrays.getQTLEGIOmpn(0, 0) == '<1'
    pass
