def is_same_tree(inorder, preorder, postorder):
    if not inorder or not preorder or not postorder:
        return False

    if len(inorder) != len(preorder) or len(inorder) != len(postorder):
        return False

    if set(inorder) != set(preorder) or set(inorder) != set(postorder):
        return False

    if len(inorder) == 1:
        return inorder[0] == preorder[0] == postorder[0]

    root_val = preorder[0]
    root_idx_inorder = inorder.index(root_val)

    left_inorder = inorder[:root_idx_inorder]
    right_inorder = inorder[root_idx_inorder + 1:]

    left_preorder = preorder[1:root_idx_inorder + 1]
    right_preorder = preorder[root_idx_inorder + 1:]

    left_postorder = postorder[:root_idx_inorder]
    right_postorder = postorder[root_idx_inorder:-1]

    return (is_same_tree(left_inorder, left_preorder, left_postorder) and
            is_same_tree(right_inorder, right_preorder, right_postorder))

# Example usage:
# inorder = [4, 2, 5, 1, 3]
# preorder = [1, 2, 4, 5, 3]
# postorder = [4, 5, 2, 3, 1]
# result = is_same_tree(inorder, preorder, postorder)
# print(result)  # Output: True
