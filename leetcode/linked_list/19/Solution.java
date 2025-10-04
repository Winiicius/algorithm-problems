class Solution {

    public static ListNode removeNthFromEnd(ListNode head, int n) {
        // Criamos um nó fictício para lidar com remoção do primeiro nó
        ListNode dummy = new ListNode(0, head);
        ListNode fast = dummy;
        ListNode slow = dummy;

        // Move 'fast' n+1 passos à frente
        for (int i = 0; i <= n; i++) {
            fast = fast.next;
        }

        // Move 'fast' até o final, junto com 'slow'
        while (fast != null) {
            fast = fast.next;
            slow = slow.next;
        }

        // 'slow' está exatamente antes do nó que será removido
        slow.next = slow.next.next;

        // Retorna o novo head
        return dummy.next;
    }

    public static void main(String[] args) {
        var listaEncadeada = new ListNode(5);
        listaEncadeada = new ListNode(4, listaEncadeada);
        listaEncadeada = new ListNode(3, listaEncadeada);
        listaEncadeada = new ListNode(2, listaEncadeada);
        listaEncadeada = new ListNode(1, listaEncadeada);

        Solution.removeNthFromEnd(listaEncadeada, 2);

        ListNode.print(listaEncadeada);
    }
}

class ListNode {
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
