
import survey
table = survey.Pregnancies()
table.ReadRecords()

def mean(seqNum):
    return float(sum(seqNum)) / len(seqNum)

def paritionRecords(table):
    first = survey.Pregnancies()
    others = survey.Pregnancies()

    for p in table.records:
        if p.outcome != 1:
            continue

        if p.birthord == 1:
            firsts.AddRecord(p)
        else:
            others.AddRecord(p)
    return first, others

def process(table):
    table.lengths = [p.prglength for p in table.records]
    table.n = len(table.lengths)
    table.mu = Mean(table.lengths)

def makeTables(data_dir='.'):
    table = survey.Pregnancies()
    table.ReadRecords(data_dir)
    firsts, others = partitinRecords(table)

    return table, firsts, others

def processTables(*tables):

    for table in tables:
        Process(table)

def Summarize(data_dir):

    table, firsts, others = makeTables(data_dir)
    processTables(firsts, others)

    print 'Number of first babies', firsts.n
    print 'Number of others', others.n

    mu1, mu2 = firsts.mu, other.mu

    print 'Mean gestation in weeks:'
    print 'First babies', mu1
    print 'Others', mu2

    print 'Difference in days', (mu1 - mu2) * 7.0

def main(name, data_dir='/Users/jfrank/dl-journey/think-stats/chapter-1'):
    Summarize(data_dir)

if __name__ == '__main__':
    import sys
    main(*sys.argv)
