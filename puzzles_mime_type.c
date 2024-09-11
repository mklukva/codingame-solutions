#define MAX_EXTENSIONS 100
#define MAX_LENGTH 100

typedef struct {
    char extension[MAX_LENGTH];
    char mime_type[MAX_LENGTH];
} MimeEntry;

int main() {
    int n, q;
    MimeEntry mime_dict[MAX_EXTENSIONS];
    int mime_count = 0;

    // Read number of mime types
    scanf("%d", &n);
    // Read number of queries
    scanf("%d", &q);

    // Read mime types into the dictionary
    for (int i = 0; i < n; i++) {
        char ext[MAX_LENGTH], mt[MAX_LENGTH];
        scanf("%s %s", ext, mt);
        
        // Convert extension to lowercase
        for (int j = 0; ext[j]; j++) {
            ext[j] = tolower(ext[j]);
        }

        // Store in the dictionary
        strcpy(mime_dict[mime_count].extension, ext);
        strcpy(mime_dict[mime_count].mime_type, mt);
        mime_count++;
    }

    // Process queries
    for (int i = 0; i < q; i++) {
        char fname[MAX_LENGTH];
        scanf("%s", fname);
        
        // Get the file extension
        char *dot = strrchr(fname, '.');
        if (dot != NULL) {
            char key[MAX_LENGTH];
            strcpy(key, dot + 1); // Get the extension part after the dot

            // Convert key to lowercase
            for (int j = 0; key[j]; j++) {
                key[j] = tolower(key[j]);
            }

            // Search for the mime type
            int found = 0;
            for (int j = 0; j < mime_count; j++) {
                if (strcmp(mime_dict[j].extension, key) == 0) {
                    printf("%s\n", mime_dict[j].mime_type);
                    found = 1;
                    break;
                }
            }

            if (!found) {
                printf("UNKNOWN\n");
            }
        } else {
            printf("UNKNOWN\n");
        }
    }

    return 0;
}