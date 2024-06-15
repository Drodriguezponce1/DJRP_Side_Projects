public class QF_Driver {
    
    public static void main(String[] args) {
        QuickFindUF qf_uf = new QuickFindUF(10);
        System.out.println(qf_uf);
        qf_uf.union(1, 2);
        qf_uf.union(3, 4);
        qf_uf.union(5, 6);
        qf_uf.union(7, 8);
        qf_uf.union(7, 9);
        qf_uf.union(2, 8);
        qf_uf.union(0, 5);
        qf_uf.union(1, 9);

        System.out.println(qf_uf);
        System.out.println(qf_uf.connection(0, 1));
    }
}
