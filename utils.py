def get_tree_info_by_key(tree_data, tree_type, key):
    
    # Check if the tree_type exists in the dictionary
    if tree_type in tree_data:
        # Check if the key exists in the tree data
        if key in tree_data[tree_type]:
            return tree_data[tree_type][key]
        else:
            return f"Key '{key}' not found for tree type '{tree_type}'"
    else:
        return f"Tree type '{tree_type}' not found."
