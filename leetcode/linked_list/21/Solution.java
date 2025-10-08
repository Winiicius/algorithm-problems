class Solution {

    public static ListNode mergeTwoLists(ListNode list1, ListNode list2) { // Minha solução

        ListNode final_list = new ListNode();
        ListNode aux = final_list;

        while (list1 != null || list2 != null) {
            if (list1 != null && list2 != null) {
                if (list1.val < list2.val) {
                    final_list.next = list1;
                    list1 = list1.next;
                } else {
                    final_list.next = list2;
                    list2 = list2.next;
                }
            } else if (list1 != null) {
                final_list.next = list1;
                list1 = list1.next;
            } else {
                final_list.next = list2;
                list2 = list2.next;
            }
            final_list = final_list.next;

        }

        return aux.next;
    }

    public static ListNode mergeTwoListsRecursive(ListNode list1, ListNode list2) { // versão recursiva
        // Caso base: se uma das listas acabou, retorna a outra
        if (list1 == null)
            return list2;
        if (list2 == null)
            return list1;

        // Escolhe o menor nó entre list1 e list2
        if (list1.val < list2.val) {
            list1.next = mergeTwoLists(list1.next, list2);
            return list1;
        } else {
            list2.next = mergeTwoLists(list1, list2.next);
            return list2;
        }
    }

    public static void main(String[] args) {
        var listaEncadeada = new ListNode(1);
        listaEncadeada.next = new ListNode(2);
        listaEncadeada.next.next = new ListNode(4);
        var listaEncadeada2 = new ListNode(1);
        listaEncadeada2.next = new ListNode(3);
        listaEncadeada2.next.next = new ListNode(4);

        ListNode.print(Solution.mergeTwoLists(listaEncadeada, listaEncadeada2));

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
