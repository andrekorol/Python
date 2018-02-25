(require 'package)

(let* ((no-ssl (and (memq system-type '(windows-nt ms-dos))

                    (not (gnutls-available-p))))

       (url (concat (if no-ssl "http" "https") "://melpa.org/packages/")))

  (add-to-list 'package-archives (cons "melpa" url) t))

(when (< emacs-major-version 24)

  ;; For important compatibility libraries like cl-lib

  (add-to-list 'package-archives '("gnu" . "http://elpa.gnu.org/packages/")))

(add-to-list 'package-archives
             '("elpy" . "https://jorgenschaefer.github.io/packages/"))
(add-to-list 'package-archives
             '("melpa" . "https://melpa.org/packages/") t)

(package-initialize)
(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-names-vector
   ["#3F3F3F" "#CC9393" "#7F9F7F" "#F0DFAF" "#8CD0D3" "#DC8CC3" "#93E0E3" "#DCDCCC"])
 '(bsh-jar "~/.myJars/bsh-2.0b4.jar")
 '(coffee-tab-width 2)
 '(company-quickhelp-color-background "#4F4F4F")
 '(company-quickhelp-color-foreground "#DCDCCC")
 '(custom-enabled-themes (quote (solarized-dark)))
 '(custom-safe-themes
   (quote
	("d677ef584c6dfc0697901a44b885cc18e206f05114c8a3b7fde674fce6180879" "8aebf25556399b58091e533e455dd50a6a9cba958cc4ebb0aab175863c25b9a4" "a8245b7cc985a0610d71f9852e9f2767ad1b852c2bdea6f4aadc12cce9c4d6d0" "599f1561d84229e02807c952919cd9b0fbaa97ace123851df84806b067666332" "5e52ce58f51827619d27131be3e3936593c9c7f9f9f9d6b33227be6331bf9881" default)))
 '(jdee-server-dir "~/.myJars")
 '(package-selected-packages
   (quote
	(company-irony jdee irony-eldoc company-irony-c-headers solarized-theme powerline whitespace-cleanup-mode coffee-mode ac-js2 js2-mode company-go go-autocomplete go-mode zenburn-theme ## flycheck-rust flycheck package-build shut-up epl git commander f dash s cask racer cargo rust-mode python-mode all-the-icons yasnippet-snippets auto-complete-c-headers auto-complete autopair)))
 '(pdf-view-midnight-colors (quote ("#DCDCCC" . "#383838")))
 '(tab-width 4))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(mode-line ((t (:foreground "#030303" :background "#bdbdbd" :box nil))))
 '(mode-line-inactive ((t (:foreground "#f9f9f9" :background "#666666" :box nil)))))

(autopair-global-mode) ;; enable autopair in all buffers

(setq show-paren-delay 0)

(show-paren-mode 1)



(setq column-number-mode t)

(require 'company)                                   ; load company mode
(require 'company-go)                                ; load company mode go backend

(add-hook 'after-init-hook 'global-company-mode)

(ac-config-default)

(defun my:ac-c-headers-init ()

  (require 'auto-complete-c-headers)

  (add-to-list 'ac-sources 'ac-source-c-headers))

(add-hook 'c++-mode-hook 'my:ac-c-headers-init)

(add-hook 'c-mode-hook 'my:ac-c-headers-init)

(require 'company-irony-c-headers)
(eval-after-load 'company
  '(add-to-list
    'company-backends '(company-irony-c-headers company-irony)))

(add-hook 'c++-mode-hook 'flycheck-mode)
(add-hook 'c-mode-hook 'flycheck-mode)

(setq-default c-basic-offset 4)


(yas-global-mode t)

(global-set-key [f8] 'neotree-toggle)
(setq neo-theme (if (display-graphic-p) 'icons 'arrow))

(global-set-key (kbd "C-h C-f") 'find-function)

(elpy-enable)

(setq rust-format-on-save t)

(add-hook 'rust-mode-hook 'cargo-minor-mode)

(add-hook 'rust-mode-hook #'racer-mode)
(add-hook 'racer-mode-hook #'eldoc-mode)

(add-hook 'racer-mode-hook #'company-mode)

(require 'rust-mode)
(define-key rust-mode-map (kbd "TAB") #'company-indent-or-complete-common)
(setq company-tooltip-align-annotations t)

;; (use-package flycheck
;;   :ensure t
;;   :init (global-flycheck-mode))

(add-hook 'flycheck-mode-hook #'flycheck-rust-setup)


(add-hook 'js-mode-hook 'js2-minor-mode)
(add-hook 'js2-mode-hook 'ac-js2-mode)

(setq js-indent-level 2)
(setq js-switch-indent-offset 2)

;; automatically clean up bad whitespace
(setq whitespace-action '(auto-cleanup))
;; only show bad whitespace
(setq whitespace-style '(trailing space-before-tab indentation empty space-after-tab))

(add-to-list 'load-path "~/.emacs.d/vendor/emacs-powerline")
(require 'powerline)
(require 'cl)


(setq powerline-color1 "grey22")
(setq powerline-color2 "grey40")

(require 'jdee)

