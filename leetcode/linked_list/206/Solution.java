import java.util.ArrayList;
import java.util.List;

/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution { // Minha solução
    public static ListNode reverseList(ListNode head) { // minha solução
        List<ListNode> lista = new ArrayList<ListNode>();

        ListNode aux = head;
        ListNode lixo = null;

        while (aux != null) { // Cria uma lista de ListNodes
            lixo = aux.next;
            aux.next = null;
            lista.add(aux);
            aux = lixo;
        }
        ListNode reverseList = new ListNode(lista.get(lista.size() - 1).val);
        aux = reverseList;

        for (int i = lista.size() - 2; i >= 0; i--) { // Percorre a lista de trás pra frente
            reverseList.next = lista.get(i);
            reverseList = reverseList.next;
        }

        return aux;

    }

    public static ListNode reverseListIA(ListNode head) { // solução IA
        ListNode prev = null;
        ListNode current = head;

        while (current != null) {
            ListNode next = current.next; // guarda o próximo
            current.next = prev; // inverte o link
            prev = current; // move prev
            current = next; // move current
        }

        return prev; // prev será o novo head
    }

    public static ListNode reverseListRecursivo(ListNode head) { // Ajuda da IA
        // Caso base: lista vazia ou com 1 elemento
        if (head == null || head.next == null) {
            return head;
        }

        // Inverte o resto da lista
        ListNode newHead = reverseList(head.next);

        // Faz o próximo nó apontar para o atual
        head.next.next = head;
        head.next = null;

        return newHead; // retorna a nova cabeça da lista
    }

    public static void main(String[] args) {
        var listaEncadeada = new ListNode(5);
        listaEncadeada = new ListNode(4, listaEncadeada);
        listaEncadeada = new ListNode(3, listaEncadeada);
        listaEncadeada = new ListNode(2, listaEncadeada);
        listaEncadeada = new ListNode(1, listaEncadeada);

        var a = Solution.reverseList(listaEncadeada);
        ListNode.print(a);
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
