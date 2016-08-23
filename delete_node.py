def delete_node(node_to_del):
    node_next = node_to_del.next

    if node_next:
        node_to_del.value = node_next.value
        node_to_del.next = node_next.next
