public class Solution {

    public static boolean hasCycle(ListNode head) {

        if (head == null || head.next == null)
            return false;

        ListNode slow = head;
        ListNode fast = head;

        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;

            if (slow == fast)
                return true;
        }

        return false;
    }

    public static void main(String[] args) {
        var listaEncadeada = new ListNode(5);
        var listaEncadeada2 = new ListNode(2);
        listaEncadeada2.next = listaEncadeada;
        listaEncadeada.next = listaEncadeada2;

        System.out.println(Solution.hasCycle(listaEncadeada));

    }
}

class ListNode { // Classe proposta pelo LeetCode ( sem o print() )

    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

    static void print(ListNode lista) {
        while (lista != null) {
            System.out.println(lista.val);
            lista = lista.next;
        }
    }

}
