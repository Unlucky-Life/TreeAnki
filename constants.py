REVIEWS_FOR_SMALL_TREE = 10
REVIEWS_FOR_FULL_TREE = 30

TREE_TYPES = {
    "oak": {
        "sprout": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
            <path d="M45,80 L55,80 L55,50 L45,50 Z" fill="#8B4513"/>
            <path d="M50,45 C20,45 30,25 50,25 C70,25 80,45 50,45" fill="#2E7D32"/>
        </svg>
        """,
        "small": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
            <path d="M45,80 L55,80 L55,40 L45,40 Z" fill="#8B4513"/>
            <path d="M50,35 C20,35 30,15 50,15 C70,15 80,35 50,35" fill="#2E7D32"/>
            <path d="M50,25 C25,25 35,5 50,5 C65,5 75,25 50,25" fill="#2E7D32"/>
        </svg>
        """,
        "full": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
            <path d="M45,90 L55,90 L55,30 L45,30 Z" fill="#8B4513"/>
            <path d="M50,25 C10,25 20,5 50,5 C80,5 90,25 50,25" fill="#2E7D32"/>
            <path d="M50,45 C20,45 30,25 50,25 C70,25 80,45 50,45" fill="#2E7D32"/>
            <path d="M50,65 C30,65 40,45 50,45 C60,45 70,65 50,65" fill="#2E7D32"/>
        </svg>
        """
    },
    "bush": {
        "sprout": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
            <path d="M45,80 L55,80 L55,60 L45,60 Z" fill="#8B4513"/>
            <circle cx="50" cy="55" r="10" fill="#558B2F"/>
        </svg>
        """,
        "small": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
            <path d="M45,80 L55,80 L55,60 L45,60 Z" fill="#8B4513"/>
            <circle cx="40" cy="55" r="15" fill="#558B2F"/>
            <circle cx="60" cy="55" r="15" fill="#558B2F"/>
        </svg>
        """,
        "full": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
            <path d="M45,80 L55,80 L55,60 L45,60 Z" fill="#8B4513"/>
            <circle cx="35" cy="55" r="20" fill="#558B2F"/>
            <circle cx="50" cy="35" r="20" fill="#558B2F"/>
            <circle cx="65" cy="55" r="20" fill="#558B2F"/>
        </svg>
        """
    },
    "flower": {
        "sprout": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
            <path d="M48,80 L52,80 L52,40 L48,40 Z" fill="#8B4513"/>
            <circle cx="50" cy="35" r="8" fill="#E91E63"/>
        </svg>
        """,
        "small": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
            <path d="M48,80 L52,80 L52,40 L48,40 Z" fill="#8B4513"/>
            <circle cx="50" cy="35" r="8" fill="#E91E63"/>
            <circle cx="42" cy="30" r="8" fill="#E91E63"/>
            <circle cx="58" cy="30" r="8" fill="#E91E63"/>
        </svg>
        """,
        "full": """
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
            <path d="M48,80 L52,80 L52,40 L48,40 Z" fill="#8B4513"/>
            <circle cx="50" cy="35" r="8" fill="#E91E63"/>
            <circle cx="42" cy="30" r="8" fill="#E91E63"/>
            <circle cx="58" cy="30" r="8" fill="#E91E63"/>
            <circle cx="42" cy="40" r="8" fill="#E91E63"/>
            <circle cx="58" cy="40" r="8" fill="#E91E63"/>
            <circle cx="50" cy="25" r="8" fill="#E91E63"/>
        </svg>
        """
    }
}